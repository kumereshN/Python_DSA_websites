def solutions(indices, K):
    if K > len(indices):
        return []
    res = []
    remainder = len(indices)//K
    training = indices[:-remainder]
    test = indices[-remainder:]
    res = [training, test, test, training]
    return res

indices = [1,2,3]
indices_2 = [1,2,3,4,5,6,7]
K = 3
solutions(indices_2, K)
