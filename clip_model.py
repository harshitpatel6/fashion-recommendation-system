import torch
import clip

device = "cuda" if torch.cuda.is_available() else "cpu"
model, _ = clip.load("ViT-B/32", device=device)

def get_text_embedding(text):
    with torch.no_grad():
        text_embedding = model.encode_text(clip.tokenize([text]).to(device))
    return text_embedding.cpu().numpy()
