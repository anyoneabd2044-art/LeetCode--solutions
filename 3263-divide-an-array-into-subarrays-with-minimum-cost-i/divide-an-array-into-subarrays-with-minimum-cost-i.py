class Solution(object):
    def minimumCost(self, nums):    
     first = nums[0]
     smallest = float('inf')
     second_smallest = float('inf')
     for x in nums[1:]:
        if x < smallest:
            second_smallest = smallest
            smallest = x
        elif x < second_smallest:
            second_smallest = x
     return first + smallest + second_smallest

