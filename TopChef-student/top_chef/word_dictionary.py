class WordDictionaryException(Exception):
    pass

class WordDictionary:

    def __init__(self):
        self.words = {}

    def load_words(self, word_path):
         
        with open(word_path) as fd:
            line = fd.readline().strip()
            title = line.split("\t")
            
            if title[0] != "WORD" or title[1] != "VALUE": #Capturamos el error para saber que estamos en el fichero correcto
                raise WordDictionaryException("This is not the file you are looking for!")
            else:
                for line in fd:
                    stripped = line.strip()
                    word = stripped.split("\t")

                    if len(word) != 2:   #Error para formato correcto en la lista: con el entero, con que solo hayan dos posiciones
                        raise WordDictionaryException("There is some error on the database!")
                    
                    try:
                        if not self.exists(word[0]): 
                            self.add_word(word[0],float(word[1]))
                        else: 
                            #Capturamos el error de palabras repetidas por si queremos capturar el error
                            self.add_word(word[0],float(word[1]))

                    except ValueError: #Capturamos el error de que la segunda palabra no sea un número
                        raise WordDictionaryException("There is some error on the database!")
                  
                    
                    

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