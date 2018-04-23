from constants import *

def total_length(text):
    return len(text)

def sentence_ratio(text):
    return len(text.split('.'))/len(text)

def word_count(text):
    return len(text.split(' '))

def avg_word_length(text):
    word_sum = sum([len(x) for x in text.split(' ')])
    word_count = len(text.split(' '))
    if word_count == 0:
        return 0
    return word_sum/word_count

def exclamation_ratio(text):
    return text.count('!')/len(text)

def single_i_ratio(text):
    s = text.split()
    i_s = s.count('i')
    I_s = s.count('I')
    if I_s == 0 and i_s == 0:
        return 0.5
    if I_s == 0:
        return 1
    return i_s/(I_s+i_s)

def capital_words_ratio(text):
    s = 0
    for word in text.split():
        if len(word) >= 2 and word.upper() == word:
            s += 1
    return s/len(text)

TEXT_FEATURES = {
    "capital_words_ratio" : capital_words_ratio,
    "single_i_ratio" : single_i_ratio,
    "exclamation_ratio" : exclamation_ratio,
    "total_length" : total_length,
    "sentence_ratio" : sentence_ratio,
    "word_count": word_count,
    "avg_word_length" : avg_word_length,
}
