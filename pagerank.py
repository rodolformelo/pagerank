"""
PageRank algorithm
References: 
https://networkx.org/documentation/stable/_modules/networkx/algorithms/link_analysis/pagerank_alg.html#pagerank
https://en.wikipedia.org/wiki/PageRank
"""

class pagerank:
    def __init__(self, M):
        """
        Parameters
        ----------
        M : numpy array
            adjacency matrix where M_i,j represents the link from 'j' to 'i', such that for all 'j'
            sum(i, M_i,j) = 1
        self.M = M"""
        self.M = M

    def pagerank_numpy(self, num_iterations: int = 100, d: float = 0.85, epsilon: float =1.0e-6):
        """PageRank

        Parameters
        ----------
        M : numpy array
            adjacency matrix where M_i,j represents the link from 'j' to 'i', such that for all 'j'
            sum(i, M_i,j) = 1
        num_iterations : int, optional
            number of iterations, by default 100
        d : float, optional
            damping factor, by default 0.85
        epsilon : float, optional
            error tolerance to check convergence

        Returns
        -------
        numpy array
            a vector of ranks such that v_i is the i-th rank from [0, 1],
            v sums to 1

        """
        import numpy as np

        N = self.M.shape[1] # Number of nodes
        if N==0:
            return []
        v = np.random.rand(N, 1)
        v = v / np.linalg.norm(v, 1)
        M_hat = (d * self.M + (1 - d) / N)
        for i in range(num_iterations):
            v_last = v
            v = M_hat @ v
            err = np.absolute(v - v_last).sum()
            if err < N * epsilon:
                return v
        return 'Did not Converge'

    def pagerank_scipy(self, num_iterations: int = 100, d: float = 0.85, epsilon: float =1.0e-6):
        """PageRank

        Parameters
        ----------
        M : numpy array
            adjacency matrix where M_i,j represents the link from 'j' to 'i', such that for all 'j'
            sum(i, M_i,j) = 1
        num_iterations : int, optional
            number of iterations, by default 100
        d : float, optional
            damping factor, by default 0.85
        epsilon : float, optional
            error tolerance to check convergence

        Returns
        -------
        numpy array
            a vector of ranks such that v_i is the i-th rank from [0, 1],
            v sums to 1

        """
        import numpy as np
        import scipy as sp
        from scipy.sparse import csr_array

        N = self.M.shape[1] # Number of nodes
        if N==0:
            return []
        A = csr_array(self.M)
        S = A.sum(axis=1)
        S[S != 0] = 1.0 / S[S != 0]
        Q = csr_array(sp.sparse.spdiags(S.T, 0, *A.shape))
        A = Q @ A
        x = np.repeat(1.0 / N, N)
        p = np.repeat(1.0 / N, N)
        dangling_weights = p
        is_dangling = np.where(S == 0)[0]
        for _ in range(num_iterations):
            xlast = x
            x = d * (x @ A + sum(x[is_dangling]) * dangling_weights) + (1 - d) * p
            # check convergence, l1 norm
            err = np.absolute(x - xlast).sum()
            if err < N * epsilon:
                return x
        return 'Do not Converge'

