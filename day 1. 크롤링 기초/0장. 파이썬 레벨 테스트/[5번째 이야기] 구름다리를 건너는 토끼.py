def crossBridge(steps):
  cnt = 0
  current = 0
  n = len(steps)
  #print(n)
  while (current <= n - 1):
    current = current + steps[current]
    cnt += 1
  return cnt
    
print(crossBridge([1, 1, 2, 3, 5]))