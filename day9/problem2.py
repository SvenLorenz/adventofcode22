import numpy as np


ds = {'U': np.array([0,1]),
      'D': np.array([0,-1]),
      'R': np.array([1,0]),
      'L': np.array([-1,0]),}

if __name__ == '__main__':
    with open('day9/input.txt', encoding="utf-8") as f:
        lines = f.readlines()
    k = np.zeros((10,2))
    visited = set()
    for line in lines:
        d, n = line.split(' ')
        for i in range(int(n)):
            k[0] += ds[d]
            for j in range(1,10):
                if np.max(np.abs(k[j] - k[j-1])) > 1: # L0 norm
                    k[j] += np.sign(k[j-1] - k[j]) # move up to 1 step in each axis
            visited.add(tuple(k[-1]))
    print(len(visited))