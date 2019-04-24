class WordDictionaryException(Exception):
    pass

class WordDictionary:

    def __init__(self):
        self.words = {}

    def load_words(self, word_path):
        # Complete this function
        pass

    def add_word(self, word, value):
        self.words[word] = value

    def exists(self, word):
        return word in self.words

    def get_value(self, word):
        return self.words[word]

    def get_words(self):
        return self.words.keys()

    def __str__(self):
        word_str = ""
        for word in self.words:
            word_str += word + ": " + str(self.words[word]) + "\n"
        return word_str

    def __len__(self):
        return len(self.words)