"""
文件说明

"""
import numpy as np
import json

# array = np.array(np.zeros(5))
# print(array)
# a = []
# for i in range(array.size):
#     a.append(array[i])
# print(str(a))
with open('best_weights.txt', 'rb') as f:
    line = f.readline()
    dict = json.loads(line)
    print(dict)
