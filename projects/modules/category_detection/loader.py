from pickle import load
import nltk

with open('projects\modules\category_detection\stopwords.txt' , 'r' , encoding='utf-8') as stopwords_file:
    stopwords = stopwords_file.readlines()
stopwords = [line.replace('\n' , '') for line in stopwords]

nltk_stopwords = nltk.corpus.stopwords.words('english')
stopwords.extend(nltk_stopwords)

with open('projects\modules\category_detection\model.h5' , 'rb') as f:
    model = load(f)

with open('projects\modules\category_detection\\normalizer.h5' , 'rb') as f:
    normalizer = load(f)

with open('projects\modules\category_detection\stem_lemmatize.h5' , 'rb') as f:
    stemmer_lemmatizer = load(f)

with open('projects\modules\category_detection\\tokenizer.h5' , 'rb') as f:
    tokenizer = load(f)

with open('projects\modules\category_detection\\vectorizer.h5' , 'rb') as f:
    vectorizer = load(f)

with open('projects\modules\category_detection\label_encoder.h5' , 'rb') as f:
    label_encoder = load(f)

