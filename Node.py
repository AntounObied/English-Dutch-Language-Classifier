"""
@author Antoun Obied
Foundations of AI
Lab 2

This class contains the definitions and functionality of a node in the tree, and a leaf node.
"""

from AttributeCalculator import no_duplicates

class Node:

    __slots__ = "attributes", "sentences", "vals", "goal", "info", "input"

    def __init__(self, sentences=None, attributes=None, goal=-1, vals=None):
        self.vals = vals
        self.sentences = sentences
        self.attributes = attributes
        self.goal = goal + len(self.attributes)
        self.vals = list(map(no_duplicates, zip(*self.sentences)))
        inputs = []
        for attribute in self.attributes:
            if attribute != self.goal:
                inputs.append(attribute)
        self.input = inputs

class Leaf:
    __slots__ = "language"

    def __init__(self, language):
        self.language = language

    def get_language(self, sentence): # Dummy variable added for recursion to continue without error
        return self.language