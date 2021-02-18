"""
@author Antoun Obied
Foundations of AI
Lab 2

This class contains all the functionality of the DT algorithm.
"""

import Node
import AttributeCalculator
from math import log


class Decision:
    __slots__ = "attributes", "child", "branches"

    def __init__(self, attributes, child=None, branches=None):
        self.attributes = attributes
        self.child = child
        self.branches = branches or {}

    def add_subtree_to_branches(self, value, subtree):
        """
        Add a subtree to a branch
        :param value:
        :param subtree:
        :return:
        """
        self.branches[value] = subtree

    def get_language(self, sentence):
        """
        Predict the language for DT algorithm
        :param sentence: Sentence to determine language
        :return: Language
        """
        att = sentence[self.attributes]
        if att not in self.branches:
            return self.child.get_language(sentence)
        else:
            return self.branches[att].get_language(sentence)


class DecisionTreeTraining:
    __slots__ = "data", "weight", "goal", "vals"

    def __init__(self, data, weight=1):
        self.data = data
        self.vals = data.vals
        self.weight = weight
        self.goal = data.goal

    def sentences_same_attribute_value(self, attributes, value, sentences):
        """
        Calculate the number of sentences with the same attribute boolean
        :param attributes: List of attributes
        :param value: Value of attribute
        :param sentences: List of sentences
        :return: Count
        """
        count = 0
        for i in range(len(sentences)):
            if sentences[i][attributes] == value:
                if self.weight == 1:
                    count += 1
                else:
                    w = 0.0
                    total_w = 0.0
                    for j in range(len(sentences[i])):
                        if sentences[i][j]:
                            w += self.weight[j]
                        total_w += self.weight[j]
                    count += (w / total_w)
        return count

    def pairs(self, attribute, sentences):
        """
        Get pair of (value, sentence) for each value
        :param attribute:
        :param sentences:
        :return: Pair of value, sentence
        """
        return [(value, [sentence for sentence in sentences if sentence[attribute] == value]) for value in
                self.vals[attribute]]

    def info_probability(self, input):
        """
        Information gain helper function
        :param input:
        :return:
        """
        p_list = AttributeCalculator.normalize_data(AttributeCalculator.remove_all_occurences(0, input))
        count = 0.0
        for p in p_list:
            count += p * log(p, 2.0)
        return count

    def info_gain(self, attribute, sentences):
        """
        Calculate information gain by reduction of entropy
        :param attribute:
        :param sentences:
        :return:
        """
        goal = self.goal
        vals = self.vals
        count = self.sentences_same_attribute_value
        number_of_sentences = len(sentences)
        sum = 0
        for (i, j) in self.pairs(attribute, sentences):
            sum += self.info_probability(
                [count(goal, v, j) for v in vals[goal]]
            ) * (len(j) / number_of_sentences)
        return self.info_probability([count(goal, v, sentences) for v in vals[goal]]) - sum

    def get_most_infogain(self, attributes, sentences):
        """
        Return the attribute with the greatest information gain
        :param attributes:
        :param sentences:
        :return:
        """
        return AttributeCalculator.get_max_key(attributes, key=lambda z: self.info_gain(z, sentences))

    def is_sentences_same_goal_class(self, sentences):
        """
        Calculates if sentences are in the same goal class
        :param sentences:
        :return:
        """
        return all(sentence[self.goal] == sentences[0][self.goal] for sentence in sentences)

    def plurality(self, sentences):
        """
        Calculates the most popular goal value
        :param sentences:
        :return:
        """
        p = AttributeCalculator.get_max_key(self.vals[self.goal],
                                            key=lambda x: self.sentences_same_attribute_value(self.goal, x, sentences))
        return Node.Leaf(p)

    def train_dt(self, sentences, attributes, tree_depth, parent_sentences=()):
        """
        Training algorithm for Decision Tree
        :param sentences:
        :param attributes:
        :param tree_depth:
        :param parent_sentences:
        :return:
        """
        if len(sentences) <= 0:
            return self.plurality(parent_sentences)
        elif len(attributes) <= 0:
            return self.plurality(sentences)
        elif self.is_sentences_same_goal_class(sentences) is True:
            return Node.Leaf(sentences[0][self.goal])
        else:
            dt = Decision(self.get_most_infogain(attributes, sentences),
                          self.plurality(sentences))

            for (i, j) in self.pairs(self.get_most_infogain(attributes, sentences), sentences):
                subtree = self.train_dt(j, AttributeCalculator.remove_all_occurences(
                    self.get_most_infogain(attributes, sentences), attributes),
                                        tree_depth + 1, sentences)
                if tree_depth != 10:
                    dt.add_subtree_to_branches(i, subtree)
            return dt
