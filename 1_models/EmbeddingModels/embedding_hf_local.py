from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")

# text = "Delhi is the capital of India."

# result = embedding.embed_query(text)
# print(result)

documents = [
    "Delhi is the capital of India",
    "Patna is the capital of Bihar",
    "Sumit wife name is Sanya"
]

result = embedding.embed_documents(documents)
print(result)