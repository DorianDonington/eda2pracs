from top_chef.word_dictionary import WordDictionary
from top_chef.adt import TopChef

a = TopChef()

a.load_data("TopChef-student/data/topchef_data.txt")
print(a)
print("succes!")