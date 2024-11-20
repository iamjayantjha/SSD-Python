import nltk
from nltk.corpus import stopwords

# Ensure stopwords are downloaded
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def read_and_process_file(file_path):
    """
    Reads a file, preprocesses it by tokenizing, normalizing, and removing stopwords.
    Returns the list of words in uppercase.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read().upper()
    except UnicodeDecodeError:
        with open(file_path, 'r', encoding='ISO-8859-1') as file:
            text = file.read().upper()

    words = [word for word in nltk.word_tokenize(text) if word.isalpha() and word not in stop_words]
    return words