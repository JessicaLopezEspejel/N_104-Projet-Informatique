
from nltk.corpus import stopwords
from nltk import word_tokenize, sent_tokenize


class PreprocessData:

    stop_words = set(stopwords.words('english'))

    def __init__(self, text):
        self.text = text

    def remove_stop_words(self):
        str_clean = ''
        lst_words = [word for word in word_tokenize(self.text) if word in stop_words]
        return ' '.join(lst_words)

