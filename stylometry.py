from collections import Counter
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords

LINES = ['-', ':', '--']

def textToString(filename):
    """read a text file and return a string"""
    with open(filename) as f: 
        return f.read()
    
    
if __name__ == "__main__":
    pass