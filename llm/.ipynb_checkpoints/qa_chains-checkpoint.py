from langchain.chains import LLMChain
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from prompting.prompt_templates import qa_prompt_template, qa_query_prompt_template
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate
from config.settings import load_api_key

load_api_key()
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
llm_flash = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

def generate_qa_queries_chain(project_information, question):
    prompt = PromptTemplate(input_variables=["question", "project_information"], template=qa_query_prompt_template)
    chain = prompt | llm_flash
    query_response = chain.invoke({"question": question, "project_information": project_information})
    if hasattr(query_response, 'content'):
        query_response = query_response.content
    return query_response.split("\n")

def get_qa_chain(project_information, question, retrieval_docs):
    prompt = PromptTemplate(input_variables=["project_information", "question", "retrieval_docs"], template=qa_prompt_template)
    chain = prompt | llm
    return chain.invoke({"project_information": project_information, "question": question, "retrieval_docs":retrieval_docs})

