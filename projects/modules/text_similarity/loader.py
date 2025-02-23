from langdetect import detect

def detect_language(text):
    try:
        return detect(text)
    except:
        return "unknown"

per_model_name = "sentence-transformers/paraphrase-multilingual-mpnet-base-v2"
en_model_name = 'all-MiniLM-L6-v2'
