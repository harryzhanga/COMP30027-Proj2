#file paths
WINDOWS_FILENAME = "data//train_raw.csv"
WINDOWS_SAMPLE_FILENAME = "data/train_raw_sample.csv"

#globally defined names for our features that we want to get from the dataset
POST_LENGTH = "post_length"
SENTENCE_COUNT = "sentence_count"
POST_COUNT = "post_count"
WORD_COUNT = "word_count"
WORD_LENGTH = "word_length"

AVG_WORD_LENGTH = "avg_word_length"
AVG_SENTENCE_LENGTH ="avg_sentence_length"
AVG_POST_LENGTH = "avg_post_length_in_characters"
PROCESSED_POST_COUNT = "processed_post_count"

INPUT_FEATURES = {
    POST_LENGTH :True,
    SENTENCE_COUNT : True,
    POST_COUNT :True,
    WORD_COUNT : True,
    WORD_LENGTH: True,
}

PROCESS_FEATURES = {
    AVG_WORD_LENGTH: True,
    AVG_SENTENCE_LENGTH : True,
    AVG_POST_LENGTH:True,
    PROCESSED_POST_COUNT: True,

}
