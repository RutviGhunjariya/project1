import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

def split_text_into_scenes(text):
    scenes = sent_tokenize(text)
    return scenes
