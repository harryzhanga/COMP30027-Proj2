from constants import *

def total_length(text):
    return len(text)

def star(text):
    return text.count("*")/len(text)

def uncapitalised_first_letter(text):
    sentences = [s.strip() for s in text.split(".") if s.strip()]
    c = 0
    for s in sentences:
        if s[0] != s[0].upper():
            c += 1
    return c/max(len(sentences), MIN)

def sentence_ratio(text):
    return len(text.split('.'))/len(text)

def word_count(text):
    return len(text.split())

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
    "star": star,
    "uncapitalised_first_letter": uncapitalised_first_letter
}

WORD_COUNT_LIST = ["lol", "gonna", "omg", "urllink", "fuck", "shit", "u", "work", "wanna", \
                    "ur", "school", "ppl", "haha", "diva", "cuz", "cos", "anyways", ":)", ":(", "coffee"\
                    "im", "stupid", "bitch", "like"]
