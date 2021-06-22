# CS50’s Introduction to Artificial Intelligence with Python
# Project 6: Language: Parser

**Aim**: Write an AI to parse sentences and extract noun phrases.

**Description**: A common task in natural language processing is parsing, the process of determining the structure of a sentence. In particular, it’s often useful to extract noun phrases out of a sentence to get an understanding for what the sentence is about. In this problem, we’ll use the context-free grammar formalism to parse English sentences to determine their structure with the aid of some tokenization functions of package *nltk*.

More info here: https://cs50.harvard.edu/ai/2020/projects/6/parser/


Usage:
```
python parser.py
```

Example:
```
$ python parser.py
Sentence: Holmes sat.
        S
   _____|___
  NP        VP
  |         |
  N         V
  |         |
holmes     sat

Noun Phrase Chunks
holmes
```
