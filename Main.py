"""
@author Antoun Obied
Foundations of AI
Lab2

This class contains the main method used to run the DT and AdaBoost training and prediction algorithms
"""

import Node
import AttributeCalculator
import sys
import pickle
from DecisionTreeNode import DecisionTreeTraining, Decision
import AdaBoost
from AdaBoost import AdaBoostTraining, WeightedDecision


def main():
    lines = []
    for i in range(11):
        lines.append(i)
    if sys.argv[1] == "train":
        training_file = sys.argv[2]
        hypothesis_file = sys.argv[3]

        sentences = []

        for line in open(training_file, encoding="utf-8-sig"):
            sentences.append(line.strip())

        sentence_attributes = AttributeCalculator.sentences_to_boolean_attributes(sentences)
        node = Node.Node(sentence_attributes, lines)

        if sys.argv[4] == "dt":
            dt = DecisionTreeTraining(node).train_dt(node.sentences, node.input, 0)
            hypothesis_out = open(hypothesis_file, "wb")
            pickle.dump(dt, hypothesis_out)

        elif sys.argv[4] == "ada":
            ada = AdaBoost.AdaBoostTraining(DecisionTreeTraining, AdaBoostTraining.stump).train_ada(node)
            hypothesis_out = open(hypothesis_file, "wb")
            pickle.dump(ada, hypothesis_out)

    elif sys.argv[1] == "predict":
        hypothesis = sys.argv[2]
        prediction_file = sys.argv[3]
        sentences = []
        hyp = open(hypothesis, "rb")
        model = pickle.load(hyp)
        file = open(prediction_file, encoding="utf-8-sig")

        for line in file:
            line = line.strip()
            sentences.append(line)

        sentences = AttributeCalculator.sentences_to_boolean_attributes_predict(sentences)

        if isinstance(model, Decision):
            for sentence in sentences:
                print(model.get_language(sentence))
        elif isinstance(model, WeightedDecision):
            for sentence in sentences:
                result = "".join(model.predict_language(sentence))
                print(result)


if __name__ == "__main__":
    main()
