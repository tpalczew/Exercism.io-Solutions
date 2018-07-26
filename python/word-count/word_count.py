import collections
import string
import wordninja

def word_count(phrase):
    phrase = phrase.lower()    # lower case
    words = wordninja.split(phrase)
    count_words = collections.Counter(words)  # count the words; it stores everything in the dictionary
    return count_words
