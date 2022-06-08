# https://leetcode.com/problems/running-sum-of-1d-array/
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

# Constraints:
# 1 <= nums.length <= 1000
# -10^6 <= nums[i] <= 10^6

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        numOfList = len(nums)
        ansList = [0] * numOfList
        for i in range(0,numOfList):
            if i==0:
                ansList[i] = nums[i]
            elif i>0:   #2,3,4...
                ansList[i] = ansList[i-1] + nums[i]
        return ansList
