import math
import matplotlib.pyplot as mpl


class Gaussian:

    def __init__(self,mu = 0 , sigma = 1):
        self.mean = mu
        self.stdev = sigma
        self.data = []

    def calculate_mean(self):

        avg = 1.0 * sum(self.data)/ len(self.data)
        self.mean = avg
        return self.mean
    

    
        