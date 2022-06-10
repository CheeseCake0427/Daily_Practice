# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Given a string s, find the length of the longest substring without repeating characters.
# Constraints:
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "qrsvbspk"
# Output: 5

# Example 3:
# Input: s = " "
# Output: 1

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        subString = {}
        subString = set()
        max_len = 0
        
        while(right < len(s)):
            if s[right] not in subString:
                subString.add(s[right])
                right += 1
                if len(subString) > max_len:
                    max_len = len(subString)
            else: # s[right] in subString:
                if len(subString) > max_len:
                    max_len = len(subString)
                while(s[left] != s[right]):
                    subString.remove(s[left])
                    left += 1
                left += 1
                right += 1
        
        return max_len
