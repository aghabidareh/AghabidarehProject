import numpy as np
from sentence_transformers import SentenceTransformer, util

def calculate_similarity(text1, text2):
    """
    return the similarity between text1 and text2
    """
    global per_model_name
    text1 = text1.split('\n\n')
    text2 = text2.split('\n\n')

    model_name = per_model_name

    model = SentenceTransformer(model_name)

    text1_embeddings = model.encode(text1 , convert_to_tensor=True)
    text2_embeddings = model.encode(text2 , convert_to_tensor=True)

    scores = []
    for emb1 in text1_embeddings:
        score = util.cos_sim(emb1, text2_embeddings)
        scores.append(score.cpu().numpy())

    similarity = np.mean(scores) * 100
    if similarity <= 0:
        similarity = 0
    elif similarity >= 100:
        similarity = 100

    return similarity