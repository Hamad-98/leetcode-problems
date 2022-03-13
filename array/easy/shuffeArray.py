"""
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].

 
"""

def shuffle(nums, n):
  s = nums[:n]
  t = nums[n:]
  l = []
  for i in range(n):
      l.append(s[i])
      l.append(t[i])

  return l
