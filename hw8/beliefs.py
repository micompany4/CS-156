# ----------------------------------------------------------------------
# Name:     beliefs
# Purpose:  Homework 8
#
# Author(s):
#
# ----------------------------------------------------------------------
"""
Module to track the belief distribution over all possible grid positions

Your task for homework 8 is to implement:
1.  update
2.  recommend_sensing
"""
import utils


class Belief(object):

    """
    Belief class used to track the belief distribution based on the
    sensing evidence we have so far.
    Arguments:
    size (int): the number of rows/columns in the grid

    Attributes:
    open (set of tuples): set containing all the positions that have not
        been observed so far.
    current_distribution (dictionary): probability distribution based on
        the evidence acquired so far.
        The keys of the dictionary are the possible grid positions
        The values represent the (conditional) probability that the
        treasure is found at that position given the evidence
        (sensor data) accumulated so far.
    """

    def __init__(self, size):
        # Initially all positions are open - have not been observed
        self.open = {(x, y) for x in range(size)
                     for y in range(size)}
        # Initialize to a uniform distribution
        self.current_distribution = {pos: 1 / (size ** 2) for pos in self.open}

    def update(self, color, sensor_position, model):
        """
        Update the belief distribution based on new evidence:  our agent
        detected the given color at sensor location: sensor_position.
        :param color: (string) color detected
        :param sensor_position: (tuple) position of the sensor
        :param model (Model object) models the relationship between the
             treasure location and the sensor data
        :return: None
        """
        # Iterate over ALL positions in the grid and update the
        # probability of finding the treasure at that position - given
        # the new evidence.
        # The probability of the evidence given the Manhattan distance
        # to the treasure id given by calling model.psonargivendist.
        # Don't forget to normalize.
        # Don't forget to update self.open since sensor_position has
        # now been observed.

        # calculate probability for all positions in the grid
        for p in self.current_distribution:
            self.current_distribution[p] *= model.psonargivendist(color, utils.manhattan_distance(p, sensor_position))

        # normalize the probabilities
        for p in self.current_distribution:
            self.current_distribution[p] /= sum(self.current_distribution.values())

        # remove that position from the set of unobserved positions because we have now observed it
        self.open.remove(sensor_position)
        # pass

    def recommend_sensing(self):
        """
        Recommend where we should take the next measurement in the grid.
        The position should be the most promising unobserved location.
        If all remaining unobserved locations have a probability of 0,
        return the unobserved location that is closest to the (observed)
        location with he highest probability.
        If there are no remaining unobserved locations return the
        (observed) location with the highest probability.

        :return: tuple representing the position where we should take
            the next measurement
        """
        # Enter your code and remove the statement below
        best_prob = -1
        index = 0
        position_list = []
        probability_list = []
        for i in self.current_distribution:
            probability_list.append(self.current_distribution[i])
        for j in self.open:
            position_list.append(self.open[j])

        count = 0
        while count < len(probability_list):
            if probability_list[count] > best_prob:
                best_prob = probability_list[count]
                index = count

        if probability_list[count] == 0:
            prob2 = -1
            count = 0
            while count < len(position_list):
                if position_list[count] > prob2:
                    prob2 = probability_list[count]
                    index = count
            return utils.closest_point(position_list[index], self.open)

        return position_list[index]
