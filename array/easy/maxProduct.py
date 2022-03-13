"""
Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
"""

def maxProduct(nums);
  max = 0
    
  for i in range(0,len(nums)):
      for j in range(i+1,len(nums)): 
          if (nums[i]-1)*(nums[j]-1) > max:
              max = (nums[i]-1)*(nums[j]-1)
  return max
