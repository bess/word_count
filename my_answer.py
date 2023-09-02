
import collections
import pdb
import string
import re

a_tale_of_two_cities = open('98-0.txt', encoding="utf8")
stopwords_from_file = open('stopwords', encoding="utf8")

def clean_word(dirty_word):
    clean = dirty_word.lower()
    clean = clean.replace(".","")
    clean = clean.replace('"',"")
    clean = clean.replace(",","")
    clean = clean.replace('“',"")
    # clean = clean.translate(str.maketrans('', '', string.punctuation))
    # clean = re.sub(r'[^\w\s]', '', clean)
    return clean

word_dict = {}
stopwords = { clean_word(i.strip()) for i in stopwords_from_file }

def add_to_dictionary(word):
    if word in stopwords:
        return
    in_dictionary = word_dict.get(word)
    if in_dictionary == None:
        word_dict[word] = 1
    else:
        word_dict[word]+=1

for line in a_tale_of_two_cities:
    words_in_line = line.split()
    for word in words_in_line:
        add_to_dictionary(clean_word(word))

# print(word_dict)
# print(stopwords_dict)

sorted_dict = sorted(word_dict.items(), key=lambda x:x[1])
print(sorted_dict)
# pdb.set_trace()
