# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

class Solution(object):
    def twoSum(self, nums, target):
        map = {}
        for i, n in enumerate(nums):
            difference = target - n
            if difference in map:
                return [map[difference], i]
            map[n] = i 