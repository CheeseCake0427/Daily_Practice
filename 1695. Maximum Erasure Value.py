# https://leetcode.com/problems/maximum-erasure-value/

# You are given an array of positive integers nums and want to erase a subarray containing unique elements. 
# The score you get by erasing the subarray is equal to the sum of its elements.
# Return the maximum score you can get by erasing exactly one subarray.
# An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

# Constraints:
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104

# Example 1:
# Input: nums = [4,2,4,5,6]
# Output: 17
# Explanation: The optimal subarray here is [2,4,5,6].

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        subnum = {}
        subnum = set()
        max_value = 0 # store history max_value total
        tmp = 0 # store current subnum total
        
        while(right < len(nums)):
            if nums[right] not in subnum:
                subnum.add(nums[right])
                tmp = tmp + nums[right]
                max_value = max(max_value, tmp)
                right += 1
            else:
                while(nums[left] != nums[right]):
                    subnum.remove(nums[left])
                    tmp = tmp - nums[left]
                    max_value = max(max_value, tmp)
                    left += 1
                left += 1
                right += 1
        
        return max_value
