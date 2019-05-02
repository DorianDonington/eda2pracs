class WordDictionaryException(Exception):
    pass


class WordDictionary:

    def __init__(self):
        """
        Arranncamos un diccionario para las palabras, que irán de key, y sus valores numéricos
        """
        self.words = {}

    def load_words(self, word_path):
        """
        Lee el documento words.txt y carga en el self.words todas las palabras clave que encuentre con su valor. Captura errores si no estamos en el 
        fichero correcto, si hay errores de formato y si el segundo ítem de una línea no es un número
        :param word_path: El path del fichero words.txt
        """

        KEYWORD1 = "WORD" 
        KEYWORD2 = "VALUE"
        TAB = "\t"

        with open(word_path) as fd: #Usamos with porque controla mejor los errores que open/close
            line = fd.readline().strip() 
            title = line.split("\t") #Utilizamos la primera línea para saber si estamos en el fichero correcto
            
            if title[0] != KEYWORD1 or title[1] != KEYWORD2 : #Capturamos el error de mal fichero
                raise WordDictionaryException("This is not the file you are looking for!")
            
            else:
                for line in fd:
                    stripped = line.strip() #We remove the endlines
                    word = stripped.split(TAB) #We take away the tabs

                    if len(word) != 2:   #Error para formato correcto en la lista: que solo hayan dos posiciones por línea
                        raise WordDictionaryException("There is some error on the database!")
                    
                    try:
                        if not self.exists(word[0]): 
                            self.add_word(word[0],float(word[1]))
                        else: 
                            #Cojemos el caso de palabras repetidas por si queremos capturar el error en el futuro. De momento hacemos lo mismo
                            self.add_word(word[0],float(word[1]))

                    except ValueError: #Capturamos el error de que la segunda palabra no sea un número
                        raise WordDictionaryException("There is some error on the database!")
                  
    def add_word(self, word, value):
        """
        Añadimos una nueva palabra al diccionario con su valor. No controlamos el error de que esté repetida porque este se controla desde una función específica
        :param word: El nuevo word 
        :param value: EL valor de la nueva palabra
        """
        self.words[word] = value

    def exists(self, word):
        """
        Sirve para controlar si una palabra está en el diccionario o no
        :param word: La palabra que checkeamos en el diccionario
        :return: True si está en el diccionario, False si no lo está
        """
        if word in self.words:
            return True
        else:
            return False
        
    def get_value(self, word):
        """
        Nos da el valor de una palabra del diccionario
        :param word: La word de la que queremos saber el valor
        :return: Un valor (float) de una palabra del diccionario
        """
        return self.words[word]

    def get_words(self):
        """
        Nos dice todas las palabras que tenemos en el diccionario
        :return: las keys del diccionario en string
        """
        return self.words.keys()

    def __str__(self):
        """
        Hace print del diccionario en el formato que se pide
        :return: Str del diccionario
        """
        word_str = ""
        for word in self.words:
            word_str += word + ": " + str(self.words[word]) + "\n"
        return word_str

    def __len__(self):
        """
        Nos dice la cantidad de palabras que hay en el diccionario
        :return: la longitud del diccionario
        """
        return len(self.words)