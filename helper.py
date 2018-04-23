from constants import *

def total_length(row):
    text = row["text"]
    return len(text)

def sentence_count(row):
    text = row["text"]
    return len(text.split('.'))

def word_count(row):
    text = row["text"]
    return len(text.split(' '))

def avg_word_length(row):
    text = row["text"]
    word_sum = sum([len(x) for x in text.split(' ')])
    word_count = len(text.split(' '))
    if word_count == 0:
        return 0
    return word_sum/word_count




INPUT_FEATURES = {
    "total_length" : total_length,
    "sentence_count" : sentence_count,
    "word_count": word_count,
    "avg_word_length" : avg_word_length,
}
