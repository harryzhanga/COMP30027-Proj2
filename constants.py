#file paths
WINDOWS_FILENAME = "data//train_raw.csv"
WINDOWS_SAMPLE_FILENAME = "data/train_raw_sample.csv"

#globally defined names for our features that we want to get from the dataset

#these are basic features
POST_LENGTH = "post_length"
SENTENCE_COUNT = "sentence_count"
POST_COUNT = "post_count"
WORD_COUNT = "word_count"
WORD_LENGTH = "word_length"

#these are more processed features
AVG_WORD_LENGTH = "avg_word_length"
AVG_SENTENCE_LENGTH ="avg_sentence_length"
AVG_POST_LENGTH = "avg_post_length_in_characters"
PROCESSED_POST_COUNT = "processed_post_count"

#the features we want to calculate (basic ones)
INPUT_FEATURES = {
    #length of the whole post, without changing anything
    POST_LENGTH :True,
    #split the posts by full stops then find length of result
    SENTENCE_COUNT : True,
    #number of posts made by this age group
    POST_COUNT :True,
    #split by spaces then count length
    WORD_COUNT : True,
    #count the number of alphabetical characters
    WORD_LENGTH: True,
}

#the features we want to calculate (processed ones)
PROCESS_FEATURES = {
    #word_length/word_count
    AVG_WORD_LENGTH: True,
    #post_length/sentence_count
    AVG_SENTENCE_LENGTH : True,
    #post_length/post_count
    AVG_POST_LENGTH:True,
    #post_count
    PROCESSED_POST_COUNT: True,
}
