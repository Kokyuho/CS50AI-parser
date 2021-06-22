import nltk
import sys

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

NONTERMINALS = """
S -> VP | VP Conj VP
VP -> NP PV | NP PV NP | NP PV NP P NP | PV NP P NP | PV NP | NP PV P NP | NP PV P NP Adv 
PV -> V | Adv V | V Adv
NP -> N | Det N | Det N P NP | Det AN
AN -> Adj N | Adj AN
"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    # String to lower case
    s = sentence.lower()

    # Split into token words
    wordList = nltk.word_tokenize(s)

    # Clean list and leave only words that contains at least one alphabetic character
    wordListClean = []
    for word in wordList:
        if word.islower() == True:
            wordListClean.append(word)

    return wordListClean


def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    # Create empty list
    NP_chunks = []

    # For each subtree that is an Noun Phrase
    for s in tree.subtrees(lambda t: t.label() == 'NP'):

        # Append to NP chunks if if does now contain other NPs
        if len(list(s.subtrees(lambda t: t.label() == 'NP'))) == 1:
            NP_chunks.append(s)

    return NP_chunks


if __name__ == "__main__":
    main()
