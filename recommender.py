from models.clip_model import get_text_embedding
from utils.pinecone_utils import search_similar_items

def get_recommendations(style_input):
    style_embedding = get_text_embedding(style_input)
    results = search_similar_items(style_embedding)
    return results
