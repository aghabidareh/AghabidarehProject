import numpy as np
from sentence_transformers import SentenceTransformer, util

from projects.modules.text_similarity.loader import *

def calculate_similarity(text1, text2):
    text1 = text1.split('\n\n')
    text2 = text2.split('\n\n')

    lang1 = detect_language(text1[0])
    lang2 = detect_language(text2[0])

    if lang1 == 'fa' and lang2 == 'fa':
        model_name = per_model_name
    else:
        return "متن مورد نظر باید فارسی باشد"

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