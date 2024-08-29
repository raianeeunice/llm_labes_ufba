from chroma import chroma_client, huggingface_ef

collection = chroma_client.get_collection(name="psychological_safety", embedding_function=huggingface_ef)

results = collection.query(
    query_texts=["As an Agile Coach, how do I deal with argumentative and uncooperative team members?"], 
    n_results=2 
)

print(results)