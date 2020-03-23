import numpy as np
import pickle as pkl

def predict(x):
  """
  :param x: matrix of images NxD
  :return: vector of class labels Nx1
  """
  X_train, Y_train = loadTrain()
  X_train = X_train.astype(int)
  x = binary(x)
  k_value = 1

  dist = distance(x, X_train)
  Y_sort = sortTrainLabels(dist, Y_train)
  prob = probability(Y_sort, k_value)

  result = np.argmax(prob, axis=1).reshape((x.shape[0], 1))
  return result

def loadTrain():
  with open('trainSet.pkl', mode = 'rb') as _f:
      return pkl.load(_f)

def binary(x):
  return (x > 0.38).astype(int)

def distance(X, X_train):
  n1 = X.shape[0]
  n2 = X_train.shape[0]
  dist = np.zeros((n1, n2))

  for i in range(n1):
      for j in range(n2):
          dist[i, j] = np.count_nonzero(X[i] != X_train[j])
  return dist

def sortTrainLabels(dist, Y_train):
  sorted = np.zeros([dist.shape[0], len(Y_train)])
  sortDist = np.argsort(dist, axis=1, kind='mergesort')

  i = 0
  for d in sortDist:
      j = 0
      for k in d:
          sorted[i][j] = Y_train[k]
          j += 1
      i += 1
  return sorted

def probability(y, k):
  prob = np.zeros([y.shape[0], 10])
  neighbours = y[:y.shape[0], :k]

  for p in range(0, 10):
      i = 0
      for n in neighbours:
          x = np.extract(n == p, n)
          prob[i][p] = len(x)/k
          i += 1
  return prob