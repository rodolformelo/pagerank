import numpy as np
from utils.read import *
from utils.power import *


class PageRank:

    def __init__(self):    
        pass

    def read_graph(self,path):
        self.A = load_graph(path)
        self.n = A.shape[0]
        self.nAt = normalize(self.A)

    def iteration(self,nodes):
        self.r = ppower_iterator(self.nAt,nodes,p=0.15, epsilon=1e-9,num_iterations=100)
    
    def print_top(self,top=10):
        sorted_scores = np.argsort(self.r)
        largest_indices = sorted_scores[::-1][:top]
        for i in largest_indices:
            print("node: {:2d}, PageRank score: {:.4f}".format(i, self.r[i]))
