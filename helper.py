def sentence_data(post):
    sentences = post.split(".")
    return sum([len(sentence) for sentence in sentences]), len(sentences)

def add_sentence_length(age, post):
    sentence_lengths, sentence_count = sentence_data(post)
    age["sentence_length_sum"] = age.get("sentence_length_sum", 0) + sentence_lengths
    age["sentence_count"] = age.get("sentence_count", 0) + sentence_count

def process_sentence_length(age):
    sentence_sum = age["sentence_length_sum"]
    sentence_count = age["sentence_count"]
    return sentence_sum/sentence_count

def add_word_length(age, post):
    words = post.split(" ")
    s = 0
    for word in words:
        s += len(word.strip())
    age["word_sum"] = age.get("word_sum", 0) + s
    age["word_count"] = age.get("word_count", 0) + len(words)

def process_word_length(age):
    return age["word_count"]/age["word_sum"]
