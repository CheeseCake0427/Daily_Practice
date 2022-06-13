# https://leetcode.com/problems/triangle/

# Given a triangle array, return the minimum path sum from top to bottom.
# For each step, you may move to an adjacent number of the row below. 
# More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

# Constraints:
# 1 <= triangle.length <= 200
# triangle[0].length == 1
# triangle[i].length == triangle[i - 1].length + 1
# -104 <= triangle[i][j] <= 104

# Example 1:
# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        min_list = [triangle[0][0]]
        tmp_list = []
        compare = 0
        
        for i in range(1, len(triangle)):
            for j in range(0, len(triangle[i])):
                if j == 0:
                    tmp = triangle[i][j] + min_list[j]
                    tmp_list.append(tmp)
                elif j == len(triangle[i])-1:
                    tmp_list.append(triangle[i][j] + min_list[j-1])
                else:
                    compare = min(min_list[j-1],min_list[j])
                    tmp_list.append(triangle[i][j] + compare)
            min_list = tmp_list.copy()
            tmp_list = []
            
        min_v = min(min_list)
        return min_v
