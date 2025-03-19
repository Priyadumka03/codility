def Solution(A, K):
  n = len(A)
  b = [None] * n
  for i in range(0,n):
    b[(i + K) % n ] = A[i]
  return b
  pass
