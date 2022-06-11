import numpy as np
from utils.read import *
from utils.power import *


class PageRank:

    def __init__(self,p=0.85,epsilon=1e-9,num_iterations=100,indirect=True):    
        self.epsilon = epsilon
        self.num_iterations = num_iterations
        self.indirect=indirect
        self.p=p

    def read_graph(self,path):
        self.A = load_graph(path,indirect=self.indirect)
        self.n = self.A.shape[0]
        self.nA = normalize(self.A)

    def iteration(self):
        self.r = power_iterator(self.nA,p=self.p, epsilon=self.epsilon,num_iterations=self.num_iterations)
        return self.r
    
    def print_top(self,top=10):
        sorted_scores = np.argsort(self.r)
        largest_indices = sorted_scores[::-1][:top]
        for i in largest_indices:
            print("node: {:2d}, PageRank score: {:.4f}".format(i, self.r[i]))


    