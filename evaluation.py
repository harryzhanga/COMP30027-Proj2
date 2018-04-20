from constants import *
import pandas as pd

def print_nicely(data):
    df = pd.DataFrame(data)

    #temporarily print it all on one line
    with pd.option_context('expand_frame_repr', False):
        print (df)
