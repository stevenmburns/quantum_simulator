from simple import *
import numpy as np



def test_a():
    for i in range(0,5):
        N = 2**i
        assert ihadamard(N).shape == (N,N)

def test_b():
    assert coord( [1,0,0,1]) == 9

def test_c():
    assert sq( 1+2j) == 5
    assert np.isclose( sq( 1+2j), np.absolute( 1+2j)**2)

def check_unitary( A):
    s = A.shape
    assert len(s) == 2 and s[0] == s[1]
    return (A.conj().T.dot(A) == np.eye(s[0])).all()

def test_d():
    assert check_unitary( hadamard(16))

def test_e():
    assert check_unitary( cnot())

def test_f():
    assert (e( 4, [0,0]) == np.array( [1,0,0,0])).all()
    assert (e( 4, [0,1]) == np.array( [0,1,0,0])).all()
    assert (e( 4, [1,0]) == np.array( [0,0,1,0])).all()
    assert (e( 4, [1,1]) == np.array( [0,0,0,1])).all()        
