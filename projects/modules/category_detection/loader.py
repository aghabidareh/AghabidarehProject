import os
from joblib import load
import nltk

"""
Loading the all of files and variables to prepare the respond!
(preprocessor , model and stopword)
using with and joblib 
also stopword from nltk
"""

current_directory = os.path.dirname(os.path.abspath(__file__))

stopwords_directory = os.path.join(current_directory , 'stopwords.txt')
model_directory = os.path.join(current_directory , 'model.h5')
normalizer_directory = os.path.join(current_directory , 'normalizer.h5')
stemmer_lemmatizer_directory = os.path.join(current_directory , 'stemmer.h5')
tokenizer_directory = os.path.join(current_directory , 'tokenizer.h5')
vectorizer_directory = os.path.join(current_directory , 'vectorizer.h5')
label_encoder_directory = os.path.join(current_directory , 'encoder.h5')

with open(stopwords_directory , 'r' , encoding='utf-8') as stopwords_file:
    stopwords = stopwords_file.readlines()
stopwords = [line.replace('\n' , '') for line in stopwords]

nltk_stopwords = nltk.corpus.stopwords.words('english')
stopwords.extend(nltk_stopwords)

with open(model_directory , 'rb') as f:
    model = load(f)

with open(normalizer_directory , 'rb') as f:
    normalizer = load(f)

with open(stemmer_lemmatizer_directory , 'rb') as f:
    stemmer_lemmatizer = load(f)

with open(tokenizer_directory , 'rb') as f:
    tokenizer = load(f)

with open(vectorizer_directory , 'rb') as f:
    vectorizer = load(f)

with open(label_encoder_directory , 'rb') as f:
    label_encoder = load(f)