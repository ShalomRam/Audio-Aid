import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize

def preprocess_text(text):
    sentences = sent_tokenize(text)
    words = [word_tokenize(sentence) for sentence in sentences]
    return words
