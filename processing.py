from helper import *
from constants import *
def get_information(ages, posts, features):
    """Gathering information from the posts and putting them into a dictionary"""
    age_dictionary = {}
    for age, post in zip(ages, posts):
        if age not in age_dictionary:
            age_dictionary[age] = {}
        curr = age_dictionary[age]
        curr["count"] = curr.get("count", 0) + 1
        if features[SENTENCE_LENGTH]:
            add_sentence_length(curr, post)
        if features[WORD_LENGTH]:
            add_word_length(curr, post)
    return age_dictionary


def process_features(age_dictionary, features):
    """Taking the information gathered by get_information and processing it more to make it useful"""

    processed_dictionary = {}
    for age in age_dictionary:
        processed_dictionary[age] = {}
        if features[SENTENCE_LENGTH]:
            processed_dictionary[age]["avg_sentence_length"] = process_sentence_length(age_dictionary[age])
        if features[WORD_LENGTH]:
            processed_dictionary[age]["avg_word_length"] = process_word_length(age_dictionary[age])
    return processed_dictionary
