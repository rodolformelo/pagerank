import numpy as np


def power_iterator(A,p=0.15, epsilon=1e-9,num_iterations=100):
    """PageRank

        Parameters
        ----------
        A : numpy array or csr matrix
            row-normalized matrix of the transpose adjacency matrix
        num_iterations : int, optional
            number of iterations, by default 100
        p : float, optional
            transport factor, by default 0.85
        epsilon : float, optional
            error tolerance to check convergence

        Returns
        -------
        numpy array
            a vector of ranks that sums to 1
        """
    n = A.shape[0] # Number of nodes
    v = np.ones(n)/n # uniform transportation
    rank = v
    for i in range(num_iterations):
        rank_last = rank
        rank = (1-p)*A.dot(rank_last) 
        s = np.sum(p) 
        rank = rank + (1 - s) * v # Handle with dead ends
        err = np.linalg.norm(rank - rank_last, 1)
        if err < epsilon:
            break
    return rank

def ppower_iterator(A, nodes, p=0.15, epsilon=1e-9,num_iterations=100):
    """PageRank

        Parameters
        ----------
        A : numpy array or csr matrix
            row-normalized matrix of the transpose adjacency matrix
        nodes: list
            list of nodes IDs
        num_iterations : int, optional
            number of iterations, by default 100
        p : float, optional
            transport factor, by default 0.85
        epsilon : float, optional
            error tolerance to check convergence

        Returns
        -------
        numpy array
            a vector of ranks that sums to 1
        """
    n = A.shape[0] # Number of nodes
    v = np.zeros(n)
    v[nodes] = 1.0/len(nodes) # uniform transportation for certain nodes
    rank = v
    for i in range(num_iterations):
        rank_last = rank
        rank = (1-p)*A.dot(rank_last) 
        s = np.sum(p) 
        rank = rank + (1 - s) * v # Handle with dead ends
        err = np.linalg.norm(rank - rank_last, 1)
        if err < epsilon:
            break
    return rank


