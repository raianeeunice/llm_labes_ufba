import pandas as pd
import os
from chroma import chroma_client, huggingface_ef

dirname = os.path.dirname(__file__)

def carregar_textos_csv(caminho_csv):
    df = pd.read_csv(caminho_csv, delimiter='|')
    # Seleciona apenas a última coluna
    ultima_coluna = df.iloc[:, -1]
    # Obtém os índices das linhas
    indices = df.index.astype(str).to_list()
    array_de_textos = ultima_coluna.to_list()
    return (array_de_textos, indices)


collection = chroma_client.create_collection(
    name="psychological_safety", 
    embedding_function=huggingface_ef, 
    get_or_create=True,
    metadata={"hnsw:space": "cosine"} # l2 is the default
)

documents, indices = carregar_textos_csv(os.path.join(dirname, './crawler/crawler_result.csv'))

collection.add(
    documents=documents,
    ids=indices
)

