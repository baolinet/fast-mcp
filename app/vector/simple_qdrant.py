import qdrant_client

client = qdrant_client.QdrantClient(":memory:")

texts = [
    "Qdrant is the best vector search engine!",
    "Loved by Enterprises and everyone building for low latency, high performance, and scale.",
]