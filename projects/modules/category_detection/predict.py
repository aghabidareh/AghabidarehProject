from projects.modules.category_detection.loader import *

def predict(text):
    """
    prepare the text to predict the response
    using preprocessor,model and nltk stopwords
    """
    title_body_normalized = normalizer.normalize(text)
    title_body_normalized_tokenized = tokenizer.tokenize_words(title_body_normalized)
    title_body_normalized_tokenized_filtered = [w for w in title_body_normalized_tokenized if not w in stopwords]
    title_body_normalized_tokenized_filtered_stemmed = [stemmer_lemmatizer.convert_to_stem(w).replace('&', ' ') for w in
                                                        title_body_normalized_tokenized_filtered]
    text = vectorizer.transform(title_body_normalized_tokenized_filtered_stemmed)
    pred = model.predict(text)[0]
    return label_encoder.classes_[pred]