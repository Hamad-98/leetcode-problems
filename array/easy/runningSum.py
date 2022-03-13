"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i])
Return the running sum of nums.
"""

def runningSum(nums):

    newArray = []
    totalSum = 0

    for num in nums:
        totalSum += num
        newArray.append(totalSum)

    return newArray
