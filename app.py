import streamlit as st
from io import BytesIO
from config.settings import load_api_key
from llm.chains import get_methodology_chain, generate_queries_chain, final_output_chain
from llm.qa_chains import get_qa_chain, generate_qa_queries_chain
from retrieval.document_retriever import retrieve_method_docs, retrieve_documents
from retrieval.fusion import reciprocal_rank_fusion
from utils import load_txt
from markdown2 import markdown
from weasyprint import HTML

# Step 1: Load configurations and models
load_api_key()

def extract_text(input_obj):
    """Ensure the input is plain text."""
    if hasattr(input_obj, 'content'):
        return input_obj.content
    if isinstance(input_obj, str):
        return input_obj
    raise ValueError(f"Unexpected input type: {type(input_obj)}")

# Define the 10 questions for the chatbot
questions = [
    "What is the primary goal of your carbon/climate project?",
    "What type of carbon credits or offsets are you aiming to generate?",
    "What is the scale of your project, and where is it located?",
    "What baseline data do you have available for your project?",
    "Have you identified the key stakeholders involved in the project?",
    "What is your timeline for project implementation and verification?",
    "What financing or funding sources have you secured or are you seeking?",
    "What potential risks have you identified, and how do you plan to mitigate them?",
    "How do you plan to measure and report the project's impact?",
    "Are there any co-benefits associated with your project?"
]

# Initialize session state
if "responses" not in st.session_state:
    st.session_state.responses = {q: "" for q in questions}
if "project_information" not in st.session_state:
    st.session_state.project_information = ""
if "pdd_output" not in st.session_state:
    st.session_state.pdd_output = ""
if "fused_docs" not in st.session_state:
    st.session_state.fused_docs = []

def go_to_chat():
    st.experimental_set_query_params(page="chat")

def go_to_main():
    st.experimental_set_query_params(page="main")

def go_to_pdd():
    st.experimental_set_query_params(page="pdd")

# Function to dynamically update project information
def update_project_information():
    st.session_state.project_information = "\n".join(
        f"{question}: {response}" for question, response in st.session_state.responses.items()
    )

# Check page state
query_params = st.experimental_get_query_params()
current_page = query_params.get("page", ["main"])[0]

# Main Application
st.title("🤖 Climate AI Assistant 🌱")
st.write("Please answer the following questions to provide details about your project.")
# Form to collect inputs
with st.form("input_form"):
    for question in questions:
        st.session_state.responses[question] = st.text_area(
            question, value=st.session_state.responses[question], height=140
        )
    
    submitted = st.form_submit_button("Generate PDD", on_click=go_to_pdd)
    asked = st.form_submit_button("Ask Questions", on_click=go_to_chat)

if current_page == "pdd":
    if submitted:
        # Compile project information
        st.session_state.project_information = "\n".join(
            f"{question}: {st.session_state.responses[question]}"
            for question in questions
        )

        with st.spinner("Processing your PDD..."):
            # Generate methodology
            methodology = get_methodology_chain(st.session_state.project_information)
            method_docs = retrieve_method_docs(extract_text(methodology))

            # Generate queries and retrieve documents
            queries = generate_queries_chain(methodology, st.session_state.project_information)
            retrieved_docs = retrieve_documents(queries)
            st.session_state.fused_docs = reciprocal_rank_fusion(retrieved_docs)

            # Generate final PDD output
            st.session_state.pdd_output = extract_text(
                final_output_chain(st.session_state.project_information, method_docs, st.session_state.fused_docs)
            )

            st.success("PDD generated successfully!")

            # Display the PDD
            st.write("### Project Design Document (PDD):")
            st.markdown(st.session_state.pdd_output)

            # Transform Markdown to HTML for PDF
            html_pdd = markdown(st.session_state.pdd_output)

            # Generate PDF for download using WeasyPrint
            pdf_buffer = BytesIO()
            HTML(string=html_pdd).write_pdf(pdf_buffer)
            pdf_buffer.seek(0)

            st.download_button(
                label="Download PDD as PDF",
                data=pdf_buffer,
                file_name="project_design_document.pdf",
                mime="application/pdf"
            )

    # Navigation Button
    st.button("Ask Questions❓", on_click=go_to_chat)

elif current_page == "chat":
    # Display project information
    st.session_state.project_information = "\n".join(
            f"{question}: {st.session_state.responses[question]}"
            for question in questions
        )
    user_question = st.text_input("Ask a question about your project:")
    if st.button("Ask"):
        # if st.session_state.fused_docs:
        with st.spinner("Fetching response..."):
            # Use retrieved documents for chat response
            queries = generate_qa_queries_chain(st.session_state.project_information, user_question)
            retrieved_docs = retrieve_documents(queries)
            fused_docs = reciprocal_rank_fusion(retrieved_docs)
            response = extract_text(get_qa_chain(st.session_state.project_information, user_question, fused_docs))
        st.write(response)
    # Navigation Button
    st.button("Back to Main Page", on_click=go_to_main)
