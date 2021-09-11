from collections import Counter
import string


def count_letters(Word):
    global count
    wordsList = string.split(Word)
    count = Counter()
    for words in wordsList:
        for letters in set(words):
            return count[letters]

Word = "The grey old fox is an idiot"
print (count_letters(Word))
