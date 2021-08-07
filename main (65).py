import numpy as np
a = np.array([45, 2, 67, 12, 14])

def sorting(x):
    for i in range(len(x)):
        swap = i + np.argmin(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])
    return x
    
print(sorting(a))