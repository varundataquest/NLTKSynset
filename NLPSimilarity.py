#Natural Language processing (NLP) tests in English

# Required and setup
# Python 3.10 or greater
# pip2 install nltk
# /Applications/Python\ 3.10/Install\ Certificates.command
# python3 -m nltk.downloader all
# In Pycharm install package nltk in UI
from pprint import pprint

import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
import string
from bs4 import BeautifulSoup

def similarity(word1, word2):
    #Synset
    syn1 = wn.synsets(word1)
    syn2 = wn.synsets(word2)

    for s1 in syn1:
        for s2 in syn2:
            print("Path similarity of: ")
            print(s1, '(', s1.pos(), ')', '[', s1.definition(), ']')
            print(s2, '(', s2.pos(), ')', '[', s2.definition(), ']')
            print("   is", s1.path_similarity(s2))
            print()

def tree(text):
    # Tokenize to words
    words = nltk.tokenize.word_tokenize(text)

    # POS tag the words
    words_tagged = nltk.pos_tag(words)

    # A simple grammar to create tree
    grammar = "NP: {<JJ><NN>}"

    # Create tree
    parser = nltk.RegexpParser(grammar)
    tree = parser.parse(words_tagged)
    pprint(tree)
    tree.draw()