# ----------------------------------------------------------------------
# Name:     classifiers
# Purpose:  Homework 9
#
# Author(s): Michael Wong, Joseph Nguyen
#
# ----------------------------------------------------------------------
"""
Your task is to implement two classifiers.

1.  A multiclass perceptron classifier
2.  A nearest neighbor classifier
"""
import numpy as np
# ----------------------------------------------------------------------
# Question 1: Multiclass perceptron
# ----------------------------------------------------------------------


class Perceptron(object):
    """
    Represent the Perceptron object
    The Perceptron object learns from the data when the train method is
    called and uses that knowledge to predict a label for new examples.

    Arguments:
    valid_labels (tuple): the unique labels that will be used.
        for digit recognition: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        for Iris: ('Iris-versicolor', 'Iris-virginica', 'Iris-setosa')
    iterations (int):  the number of iterations to be used.

    Attributes:
    weights (dict): tke keys are labels and the values are the weight
        vectors corresponding to each label.
    valid_labels (tuple): the unique labels that will be used.
        for digit recognition: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        for Iris: ('Iris-versicolor', 'Iris-virginica', 'Iris-setosa')
    iterations (int):  the number of iterations to be used.
    """
    def __init__(self, labels, iterations):
        self.weights = {}
        self.valid_labels = labels
        self.iterations = iterations

    def init_weights(self, num_features):
        """
        Initialize the weight vector corresponding to each label.
        The weights for all the features are initialized to 0.
        :param num_features (int): number of features (including bias)
        :return: None
        """
        for each_label in self.valid_labels:
            self.weights[each_label] = np.zeros(num_features)


    def train(self, data):
        """
        Train the perceptron with the given labelled data
        :param data (list of Example objects) list of training examples
        :return: None
        """
        num_features = data[0].number_of_features
        self.init_weights(num_features)
        for iteration in range(1, self.iterations+1):
            print('iteration:', iteration)
            for example in data:
                self.update_weights(example)

    def update_weights(self, example):
        """
        Update the Perceptron weights based on a single training example
        :param example (Example): representing a single training example
        :return: None
        """
        predicted_label = self.predict(example)
        actual_label = example.label
        if predicted_label != actual_label:
            self.weights[predicted_label] -= example.fvector
            self.weights[actual_label] += example.fvector

    def predict(self, example):
        """
        Predict the label of the given example
        :param example (Example): representing a single example
        :return: label: A valid label
        """
        return max(self.weights, key=lambda x: self.weights.get(x) @ example.fvector)


# ----------------------------------------------------------------------
# Question 2: Nearest Neighbor
# ----------------------------------------------------------------------

def predict_knn(data, example, k):
    """
    Classify an example based on its nearest neighbors
    :param data: list of training examples
    :param example: (Example object) example to classify
    :param k: number of nearest neighbors to consider
    :return: label: valid label from the given dataset
    """
    # Enter your code and remove the statement below
    i = 0
    training = []  # a list of tuples containing the label and distance of all the training examples
    while i < len(data):
        training.append((data[i].label, example.distance(data[i])))
        i = i + 1

    training.sort(key=lambda x: x[1])    # sorts the training data from shortest to largest distance

    j = 0
    neighbors = []  # a list containing the labels of the k nearest neighbors
    while j < k:
        neighbor_label, neighbor_dist = training[j]
        neighbors.append(neighbor_label)
        j = j + 1

    return max(set(neighbors), key=neighbors.count)     # return the most reoccurring label
