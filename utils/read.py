import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse import spdiags

def read_graph(X, dense=False, indirected=False):
    """Read directed graph
        Parameters
        ----------
        X: numpy array with ordered IDs from vertex i to vertex j 
        Returns
        -------
        A: dense numpy array or csr sparse matrix
        """
    src = X[:,0]
    dst = X[:,1]
    n = int(np.amax(X[:,:2])) + 1
    unweighted = np.ones(X.shape[0]) # creating a one value weight for each link
    if dense:
        A = np.zeros((n, n))
        A[src,dst] = 1 #unweigted
        if indirected:
            A[dst,src] = 1
    else:
        A = csr_matrix((unweighted,(src,dst)),shape=(n,n),dtype=int)
        if indirected:
            A = A + A.T 
    return A        



def load_graph(path, dtype=int, dense=False, indirected=True):
    """Read directed graph
        Parameters
        ----------
        path: string
            path to a txt file with link information (ID src => ID dst) for each line
        Returns
        -------
        A: numpy array or csr matrix
            dense numpy array if dense=True, otherwise CSR_matrix
        """
    X = np.loadtxt(path,dtype=dtype)
    A = read_graph(X, dense=dense, indirected=indirected)
    return A


def normalize(A):
    """Read directed graph
        Parameters
        ----------
        A: numpy array or csr sparse matrix
            Graph adjacency matrix 
        Returns
        -------
        A: numpy array or csr matrix
            Transposed row-normalized adjacency matrix
        """
    # First we have to create diagonal matrix 'D' with the inverse out degree
    # We have also to take into account dead ends to avoid division by 0
    d = A.sum(axis=1)
    if type(A)==scipy.sparse.csr.csr_matrix:
        d = np.asarray(d).flatten() # transform csr matrix into vector
        invd = 1.0 / np.maximum(d, np.ones(d.shape[0])) # Inverse d taking into account deadends
        invD = spdiags(data = invd, diags=0, m=d.shape[0], n=d.shape[0])
        # compute row normalized adjacency matrix by nA = invD * A
        nAT = invD.dot(A).T
    else:
        invd = 1.0 / np.maximum(d, np.ones(d.shape[0])) # Inverse d taking into account deadends
        invD = np.diag(invd) 
        # compute row normalized adjacency matrix by nA = invD * A
        nAT = invD.dot(A).T
    return nAT
    
