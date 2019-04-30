from top_chef.word_dictionary import WordDictionary
from top_chef.adt import TopChef

a = TopChef()
word_dict = WordDictionary()
print(word_dict)
print("hi")
word_dict.load_words("TopChef-student/data/words.txt")
print(word_dict)

a.load_data("TopChef-student/data/topchef_data.txt")
