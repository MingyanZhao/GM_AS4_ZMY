import pickle
import numpy as np
import matplotlib.pyplot as plt
import image




with open('A.pickle', 'rb') as f:
  letter_set = pickle.load(f)

m = letter_set.shape[0]
train_set = letter_set[:m * 0.9, :, :]
cross_set = letter_set[m*0.9:m,:]

with open('A_test.pickle', 'rb') as f:
  test_set = pickle.load(f)

def flattenData(set):
  for i in range(set.shape[0]):
    set[i, :, :].flatten()



'''
print(letter_set.shape)
arr = np.array(letter_set[2, :, :])
print(arr)
im = Image.fromarray(arr*500)
im.show()
'''

print(train_set.shape)
print(cross_set.shape)
print(test_set.shape)

flattenData(test_set)
print(test_set[0])

