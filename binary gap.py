def Solution(N):
  C = bin(N) [2:]
  b = 0
  maxb = 0
  for k in C:
    if int (k) == 0:
      b += 1
    elif int (k) == 1:
      maxb = max(b, maxb)
      b = 0
  return maxb
