from constants import *

def post_length(curr, post):
    curr[POST_LENGTH] = curr.get(POST_LENGTH, 0) + len(post)

def sentence_count(curr, post):
    curr[SENTENCE_COUNT] = curr.get(SENTENCE_COUNT, 0) + len(post.split('.'))

def post_count(curr, post):
    curr[POST_COUNT] = curr.get(POST_COUNT, 0) + 1

def word_count(curr, post):
    curr[WORD_COUNT] = curr.get(WORD_COUNT, 0) + len(post.split())

def word_length(curr, post):
    length = len([x for x in post if x.isalpha()])
    curr[WORD_LENGTH] = curr.get(WORD_LENGTH, 0) + length

def avg_word_length(d, age):
    d[AVG_WORD_LENGTH] = age[WORD_LENGTH]/age[WORD_COUNT]

def avg_sentence_length(d, age):
    d[AVG_SENTENCE_LENGTH] = age[POST_LENGTH]/age[SENTENCE_COUNT]

def avg_post_length(d, age):
    d[AVG_POST_LENGTH] = age[POST_LENGTH]/age[POST_COUNT]

def processed_post_count(d, age):
    d[PROCESSED_POST_COUNT] = age[POST_COUNT]

FUNCTIONS = {
    POST_LENGTH: post_length,
    POST_COUNT: post_count,
    SENTENCE_COUNT: sentence_count,
    WORD_COUNT: word_count,
    WORD_LENGTH: word_length,

    AVG_WORD_LENGTH: avg_word_length,
    AVG_SENTENCE_LENGTH: avg_sentence_length,
    AVG_POST_LENGTH: avg_post_length,
    PROCESSED_POST_COUNT: processed_post_count
}
