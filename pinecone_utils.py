import pinecone
from config import PINECONE_API_KEY, PINECONE_ENVIRONMENT

pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENVIRONMENT)
index = pinecone.Index("fashion-recommender")

def search_similar_items(embedding):
    results = index.query(embedding.tolist(), top_k=5, include_metadata=True)
    return [{"image_url": match["metadata"]["image_url"], "description": match["metadata"]["description"]}
            for match in results["matches"]]
