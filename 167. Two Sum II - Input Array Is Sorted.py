# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. 
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.

# Example 1:
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ptr1 = 0
        ptr2 = len(numbers)-1

        for i in range(0,len(numbers)):
            v1 = numbers[ptr1]
            v2 = numbers[ptr2]
            sum = v1 + v2
            
            if sum > target:
                ptr2 -= 1
            elif sum < target:
                ptr1 += 1
            else: # sum == target
                ans = [ptr1+1,ptr2+1]
                return ans
