"""Generate Markov text from text files."""


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
    key =  choice(list(chains.keys())) #get random key
    final_words = [key[0],key[1]] #start final list with selected key tuple values
    random_value = choice(chains[key]) #get random value from selected key tuple values
  
    while random_value is not None: 
       
        final_words.append(random_value) #append random value from selected key tuple to final list
        key = (key[1], random_value) #make tuple using second word of selected key and random value of selected key
        random_value = choice(chains[key]) #get random value

    return ' '.join(final_words) #convert final list into a string with spaces in between elements


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
