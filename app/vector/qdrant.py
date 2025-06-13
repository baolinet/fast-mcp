from transformers import AutoTokenizer, AutoModel
import torch
import qdrant_client
from qdrant_client.http import models as qdrant_models

# 加载Qwen-3模型和分词器
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen-3")
model = AutoModel.from_pretrained("Qwen/Qwen-3")

# 初始化Qdrant客户端
client = qdrant_client.QdrantClient("http://localhost:6333")  # 假设Qdrant在本地运行

# 创建Qdrant集合
collection_name = "my_collection"
client.recreate_collection(
    collection_name=collection_name,
    vectors_config=qdrant_models.VectorParams(size=768, distance="Cosine")
)

def embed_text(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    embeddings = outputs.last_hidden_state.mean(dim=1).squeeze().numpy()
    return embeddings

# 示例文本
texts = [
    "Qdrant is the best vector search engine!",
    "Loved by Enterprises and everyone building for low latency, high performance, and scale.",
]

# 将文本嵌入并存储到Qdrant
for idx, text in enumerate(texts):
    vector = embed_text(text)
    client.upsert(
        collection_name=collection_name,
        points=[
            qdrant_models.PointStruct(
                id=idx,
                vector=vector,
                payload={"content": text}
            )
        ]
    )

def search_and_rerank(query):
    # 生成查询的嵌入
    query_vector = embed_text(query)

    # 从Qdrant检索最相似的文档
    search_result = client.search(
        collection_name=collection_name,
        query_vector=query_vector,
        limit=5
    )

    # 提取文档内容
    documents = [hit.payload["content"] for hit in search_result]

    # 计算相似度并重排序
    document_embeddings = [embed_text(doc) for doc in documents]
    similarities = np.dot(document_embeddings, query_vector)
    ranked_docs = sorted(zip(documents, similarities), key=lambda x: x[1], reverse=True)

    return ranked_docs

# 示例查询
query = "What is the best vector search engine?"
ranked_documents = search_and_rerank(query)

# 输出排序结果
for doc, score in ranked_documents:
    print(f"Document: {doc}, Similarity: {score:.4f}")