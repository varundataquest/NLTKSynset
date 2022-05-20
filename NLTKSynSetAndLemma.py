#Natural Language processing (NLP) tests in English

# Required and setup
# Python 3.10 or greater
# pip2 install nltk
# /Applications/Python\ 3.10/Install\ Certificates.command
# python3 -m nltk.downloader all
# In Pycharm install package nltk in UI
from pprint import pprint

from NLPSimilarity import similarity
from NLPSimilarity import tree

import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
import string
from bs4 import BeautifulSoup


def wiki_synset_lemma():
    url = "https://en.wikipedia.org/wiki/Open_source"
    text = BeautifulSoup(download_text(url), "html.parser").get_text()
    # Tokenize to words
    words = tokenize_word(text)


    # Remove Stop words
    stop_words = get_stopwords('english')

    # Remove Punctuations
    # punctuations, add extra puncations to list and remove them all
    punctuations = get_punctuations('english')
    punctuations.append('”')
    punctuations.append('’')
    punctuations.append('“')
    words = [word for word in words if word not in punctuations]

    print("Downloaded and split in to words ...")
    print(len(words), 'words:', words)

    #print the Synset for first word we downloaded
    word = words[0]
    print("Synset:", wn.synsets(word))

    #print the first lemma for the first word we downloaded
    print("lemma:", wn.synsets(word)[0].lemmas())


def wordnet_ops(word):
    #Synset
    print(wn.synset(word).definition())
    #lemma
    [str(lemma.name()) for lemma in wn.synset(word).lemmas()]

    #languages
    print( sorted(wn.langs()))
    print( wn.synset(word).lemma_names('jpn'))


def hypernyms(synset):
    return synset.hypernyms()

def printSynsettree(word):
    synsets = wn.synsets(word)
    for synset in synsets:
        print(synset.name() + " tree:")
        pprint(synset.tree(rel=hypernyms))
        print()

def download_text(url):
    import urllib.request
    text = urllib.request.urlopen(url).read().decode()
    return text



def tokenize_word(text):
    words = word_tokenize(text)
    return words


def get_stopwords(language):
    stop_words = stopwords.words(language)
    return stop_words


def get_punctuations(language):
    if language == 'english':
        punctuations = list(string.punctuation)
    return punctuations


if __name__ == '__main__':
    #wordnet_ops('dog.n.01')
    #printSynsettree('soccer')
    # wiki_synset_lemma()

    similarity('Donkey', 'Horse')
    text = "Cricket is fun"
    tree(text)



