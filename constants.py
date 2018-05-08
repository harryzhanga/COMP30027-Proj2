from nltk import Nonterminal, nonterminals, Production, CFG
from nltk.parse import RecursiveDescentParser
import nltk
#file paths

WINDOWS_FILENAME = "data//train_raw.csv"
WINDOWS_SAMPLE_FILENAME = "data/train_raw_sample.csv"
MIN = 0.01
AGE = "the_age"
N = 3
ENGLISH = set(w.lower() for w in nltk.corpus.words.words())
