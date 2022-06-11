import sys
import os.path
import fire
from rank.prank import PageRank
import numpy as np


def query(indirect,
            input_path,
            output_path,
            p=0.85,
            epsilon=1e-9,
            max_iters=100,
            top=10):
    '''
    inputs
        indirect: : bool
            if indirect graph or not
        input_path : str
            path for the graph data
        output_path : str
            path for storing the page rank score vector
        p : float
            probability to continue the random walk or 1 minus the probability to transportation
        epsilon : float
            error tolerance for power iteration
        max_iters : int
            maximum number of iterations for power iteration
        top : int
            number of the top results to print
    outputs
        r : ndarray
            RWR score vector
    '''
    pagerank = PageRank(p=p,epsilon=epsilon,num_iterations=max_iters,indirect=indirect)
    pagerank.read_graph(input_path)
    r = pagerank.iteration()
    node_ids = np.arange(0, pagerank.n)
    write_vector(output_path, node_ids, r)
    print_top(r,top=top)

def print_top(r,top):
    sorted_scores = np.argsort(r)
    largest_indices = sorted_scores[::-1][:top]
    for i in largest_indices:
        print("node: {:2d}, PageRank score: {:.10f}".format(i, r[i]))

def write_vector(output_path, node_ids, r):
    data = np.vstack((node_ids, r)).transpose()
    np.savetxt(output_path, data, fmt='%d %e')

def main():
    fire.Fire(query)

if __name__ == "__main__":
    sys.exit(main())

