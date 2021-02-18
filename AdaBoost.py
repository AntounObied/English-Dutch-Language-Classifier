"""
@author Antoun Obied
Foundations of AI
Lab 2

This class contains all the functionality the AdaBoost algorithm
"""

from collections import defaultdict

from AttributeCalculator import normalize_data
import math

class WeightedDecision:

    __slots__ = "hypothesis", "weight"

    def __init__(self, hypothesis, weight):
        self.hypothesis = hypothesis
        self.weight = weight

    def item_with_greatest_weight(self, items, weights):
        """
        Returns the item with the greatest weight
        :param items: List of items
        :param weights: Weights of items
        :return:
        """
        d = defaultdict(int)
        for item, weight in zip(items, weights):
            d[item] += weight
        return max(d, key=d.__getitem__)

    def predict_language(self, sentence):
        """
        Predicts the language based on analysis of the tree
        :param sentence: Sentence that is analyzed
        :return: The item, and weight with the greatest say
        """
        items, weights = self.item_with_greatest_weight((i.get_language(sentence) for i in self.hypothesis), self.weight)
        return items, weights

class AdaBoostTraining:

    __slots__ = "training", "stump"

    def __init__(self, training, stump):
        self.training = training
        self.stump = stump

    def train_ada(self, data):
        """
        Method to train the AdaBoost algorithm
        :param data: Data used for training
        :return: Returns hypothesis model
        """
        goal = data.goal
        sentences = data.sentences
        hyp = []
        weight_list = []
        e = 1/(2 * len(sentences))
        weights = [(1 / len(sentences)) for i in sentences]
        for i in range(3):
            stump_hypothesis = self.training(data, weights).train_dt(data.sentences, data.input, 0)

            error_vals = []
            hyp.append(stump_hypothesis)
            for sentence, weight in zip(sentences, weights):
                if sentences[goal] != stump_hypothesis.get_language(sentence):
                    error_vals.append(weight)
            error = sum(error_vals)
            m = min(1 - e, error)
            error = max(e, m)

            for k, sentence in enumerate(sentences):
                if sentence[goal] == stump_hypothesis.get_language(sentence):
                    weights[k] = weights[k] * (error / (1 - error))
            weights = normalize_data(weights)
            temp = math.log((1 - error) / error)
            weight_list.append(temp)
        return WeightedDecision(hyp, weight_list)