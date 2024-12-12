from embeddings.embedding_loader import load_embedding_model
from vectordb.vectordb_handler import load_vector_dbs, load_vector_dbs_qa

embedding_model = load_embedding_model()
method_retriever, proj_retriever = load_vector_dbs(embedding_model)

def retrieve_method_docs(methodology):
    return method_retriever.get_relevant_documents(methodology)

def retrieve_documents(queries):
    return [proj_retriever.get_relevant_documents(query) for query in queries]


method_retriever_qa, proj_retriever_qa = load_vector_dbs_qa(embedding_model)
def retrieve_method_docs_qa(methodology):
    return method_retriever_qa.get_relevant_documents(methodology)

def retrieve_documents_qa(queries):
    return [proj_retriever_qa.get_relevant_documents(query) for query in queries]