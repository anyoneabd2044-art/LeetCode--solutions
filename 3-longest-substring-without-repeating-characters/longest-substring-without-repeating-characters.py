class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_map = {}
        left = 0
        max_res = 0
        
        for right, char in enumerate(s):
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1
            char_map[char] = right
            max_res = max(max_res, right - left + 1)
            
        return max_res
        