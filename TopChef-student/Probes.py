from top_chef.word_dictionary import WordDictionary
from top_chef.adt import TopChef

a = TopChef()
word_dict = WordDictionary()
a.load_data("TopChef-student/data/topchef_data.txt")
word_dict.load_words("TopChef-student/data/words.txt")
a.compute_scores(word_dict)
a = a.reviews.min_score()
print(a)