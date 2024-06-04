import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')


def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    return tokens


def recognize_intent(tokens):
    if 'reminder' in tokens:
        return 'set_reminder'
    elif 'weather' in tokens:
        return 'get_weather'
    elif 'what is' in tokens or 'who is' in tokens:
        return 'general_query'
    else:
        return 'unknown'
