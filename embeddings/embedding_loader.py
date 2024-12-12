from langchain_community.embeddings import HuggingFaceBgeEmbeddings

def load_embedding_model(model_name="Snowflake/snowflake-arctic-embed-m-v1.5", device="cpu"):
    model_kwargs = {"device": device}
    encode_kwargs = {"normalize_embeddings": True}
    embedding_model = HuggingFaceBgeEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )
    return embedding_model
