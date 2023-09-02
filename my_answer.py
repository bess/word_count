
import collections
import pdb
import string
import re

a_tale_of_two_cities = open('98-0.txt', encoding="utf8")
stopwords_from_file = open('stopwords', encoding="utf8")

# Note: Using more thorough punctuation cleaning works but gives a different
# word count answer, so I switched to only removing the same punctuation the
# example problem used.
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

sorted_dict = sorted(word_dict.items(), key=lambda x:x[1], reverse=True)
for i in range(0,11):
    print(sorted_dict[i])

# Top word count values in the provided A Tale of Two Cities file are:
# ('said', 642)
# ('mr', 616)
# ('one', 420)
# ('lorry', 313)
# ('will', 290)
# ('upon', 289)
# ('little', 264)
# ('man', 259)
# ('defarge', 259)
# ('time', 236)
# ('hand', 231)

# This matches the answer provided.
# pdb.set_trace()
