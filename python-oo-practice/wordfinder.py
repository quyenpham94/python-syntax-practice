"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """Program for finding random words from dictionary.
    >>> wf = WordFinder("words.txt")
    235886 words read

    >>> wf.random()
    'sirki'

    >>> wf.random()
    'palistrophia'

    """
    def __init__(self, path):
        """Read dictionary and report number of items read."""
        dict_file = open(path)
        self.words = self.parse(dict_file)
        print(f"{len(self.words)} word leads")
    
    def parse(self, dict_file):
        """Parse dict_file -> list of words."""
        return [w.strip() for w in dict_file]
    
    def random(self):
        """Return random word."""
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """Specilized WordFinder that excludes blank lines/comments.
    >>> wf = SpecialWordFinder("specialwords.txt")
    6 words read

    >>> wf.random()
    'eating'

    >>> wf.random()
    'waiting'

    """
    def parse(self, dict_file):
        """Parse dict_file -> list of words that doesnot contain blanks/comments """
        return [w.strip() for w in dict_file if w.strip() and not w.startswith("#")] 