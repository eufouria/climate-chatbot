from langchain_community.vectorstores import FAISS

def load_vector_dbs(embedding_model):
    method_path = "vectordb/vectordb_guideline"
    proj_path = "vectordb/vectordb_snowflake"
    
    method_vectordb = FAISS.load_local(method_path, embeddings=embedding_model, allow_dangerous_deserialization=True)
    proj_vectordb = FAISS.load_local(proj_path, embeddings=embedding_model, allow_dangerous_deserialization=True)
    
    method_retriever = method_vectordb.as_retriever(search_kwargs={"k": 1})
    proj_retriever = proj_vectordb.as_retriever(search_kwargs={"k": 3})
    
    return method_retriever, proj_retriever


def load_vector_dbs_qa(embedding_model):
    method_path = "vectordb/vectordb_guideline"
    proj_path = "vectordb/vectordb_snowflake"
    
    method_vectordb = FAISS.load_local(method_path, embeddings=embedding_model, allow_dangerous_deserialization=True)
    proj_vectordb = FAISS.load_local(proj_path, embeddings=embedding_model, allow_dangerous_deserialization=True)
    
    method_retriever = method_vectordb.as_retriever(search_kwargs={"k": 1})
    proj_retriever = proj_vectordb.as_retriever(search_kwargs={"k": 5})

    return method_retriever, proj_retriever
