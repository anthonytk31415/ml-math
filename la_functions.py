import numpy as np

def calculate_eigenvectors(arr): 
    det = np.linalg.det(arr)
    e_val, e_vec = np.linalg.eig(arr)
    inv = np.linalg.inv(arr)

    res = [arr, det, e_val, e_vec, inv]
    tags = ["matrix", "determinant", "eigenvalues", "eigenvectors", "inverse"]
    for tag, output in zip(tags, res): 
        print("{}: {}".format(tag, output))
    return res