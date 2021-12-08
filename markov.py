"""Generate Markov text from text files."""

import random

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(file_path).read()

    return contents


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    words = text_string.split()
    words.append(None)

    chains = {}
    value_list = []

    for i in range(len(words)-2):
        key = (words[i], words[i+1])
        value = words[i+2]
        if key in chains:
            chains[key].append(value)
        else:
            chains[key] = [value]   
 
    return chains


def make_text(chains):
    """Return text from chains."""
    key =  choice(list(chains.keys()))
    final_words = [key[0],key[1]]
    randomValue = choice(chains[key])
  
    while randomValue is not None:
        key = (key[1], randomValue)
        final_words.append(randomValue)
        randomValue = choice(chains[key])

    return ' '.join(final_words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
