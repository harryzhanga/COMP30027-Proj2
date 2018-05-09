from nltk import Nonterminal, nonterminals, Production, CFG
from nltk.parse import RecursiveDescentParser
import nltk
#file paths

WINDOWS_FILENAME = "data//train_raw.csv"
WINDOWS_SAMPLE_FILENAME = "data/train_raw_sample.csv"
DEV_FILENAME = "data//dev_raw.csv"
MIN = 0.01
AGE = "the_age"
N = 2
TOP_10_FILENAME = "data//train_top10.csv"
ENGLISH = set(w.lower() for w in nltk.corpus.words.words())
SAVE_LOCATION = "data/all_results.csv"
TEST_FILENAME = "data//test_raw.csv"
