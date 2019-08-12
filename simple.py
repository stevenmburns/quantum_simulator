import numpy as np

def ihadamard( N):
    if N == 1:
        return np.array( [[1]])
    elif N == 2:
        return np.array( [[ 1, 1],
                          [ 1,-1]])
    elif N > 2:
        N2 = N//2
        assert 2*N2 == N
        return np.kron( ihadamard( N//2), ihadamard( 2))

def hadamard( N):
    return ihadamard( N) / np.sqrt(N)

def cnot():
    return np.array( [[1,0,0,0],
                      [0,1,0,0],
                      [0,0,0,1],
                      [0,0,1,0]])

def sq( v):
    return np.conj(v)*v

def coord( lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[-1] + 2*coord( lst[:-1])

def e( N, lst):
    c = coord(lst)
    return np.array( [ 1 if i == c else 0 for i in range(N)])
