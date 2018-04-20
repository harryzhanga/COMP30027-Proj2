from helper import *
from constants import *



def get_information(ages, posts):
    """Gathering information from the posts and putting them into a dictionary"""
    age_dictionary = {}
    for age, post in zip(ages, posts):
        if age not in age_dictionary:
            age_dictionary[age] = {}
        curr = age_dictionary[age]
        for feature in INPUT_FEATURES:
            func = FUNCTIONS[feature]
            func(curr, post)
    return age_dictionary


def process_features(age_dictionary):
    """Taking the information gathered by get_information and processing it more to make it useful"""
    processed_dictionary = {}
    for age in age_dictionary:
        processed_dictionary[age] = {}
        curr = processed_dictionary[age]
        for feature in PROCESS_FEATURES:
            func = FUNCTIONS[feature]
            func(curr, age_dictionary[age])
    return processed_dictionary
