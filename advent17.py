import itertools

nums = [50,44,11,49,42,46,18,32,26,40,21,7,18,43,10,47,36,24,22,40]
ctr = 0
mini = 100

for i in range(0, len(nums)+1):
  for subset in itertools.combinations(nums, i):
    if (sum(subset) == 150 and len(subset) < mini):
        mini = len(subset)
        break

for subset in itertools.combinations(nums, mini):
  if sum(subset) == 150:
    ctr = ctr + 1
    
print ctr
