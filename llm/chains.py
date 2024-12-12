from langchain.chains import LLMChain
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from prompting.prompt_templates import methodology_prompt_template, project_prompt_template, final_output_prompt_template
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate
from config.settings import load_api_key

load_api_key()
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
llm_flash = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

def get_qa_chain(project_information):
    prompt = PromptTemplate(input_variables=["project_information", "query"], template=qa_prompt_template)
    chain = prompt | llm
    return chain.invoke({"project_information": project_information, "query": query})

def get_methodology_chain(project_information):
    prompt = PromptTemplate(input_variables=["project_information"], template=methodology_prompt_template)
    chain = prompt | llm_flash
    return chain.invoke({"project_information": project_information})

def generate_queries_chain(methodology, project_information):
    prompt = PromptTemplate(input_variables=["methodology", "project_information"], template=project_prompt_template)
    chain = prompt | llm_flash
    query_response = chain.invoke({"methodology": methodology, "project_information": project_information})
    if hasattr(query_response, 'content'):
        query_response = query_response.content
    return query_response.split("\n")

def final_output_chain(project_information, method_docs, project_docs):
    prompt = PromptTemplate(
        input_variables=["project_information", "method_docs", "project_docs"],
        template=final_output_prompt_template
    )
    chain = prompt | llm
    return chain.invoke({
        "project_information": project_information,
        "method_docs": "\n".join([doc.page_content for doc in method_docs]),
        "project_docs": "\n".join([doc[0].page_content for doc in project_docs])
    })
