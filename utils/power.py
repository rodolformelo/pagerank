import numpy as np
import scipy


def power_iterator(A,p=0.85, epsilon=1e-9,num_iterations=100):
    """PageRank

        Parameters
        ----------
        A : numpy array or cco matrix
            row-normalized adjacency matrix
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
    v = np.ones(n)/n # uniform vector
    r = v
    for i in range(num_iterations):
        r_last = r
        r = p*(A.T).dot(r_last) 
        s = np.sum(r.T) 
        r = r + (1 - s) * v # Handle with dead ends
        err = np.linalg.norm(r - r_last, 1)
        if err < epsilon:
            break
    return r




