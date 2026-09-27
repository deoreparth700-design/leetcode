class Solution(object):
    def buildArray(self, nums):
        value = []

        for i in range(len(nums)):
            value.append(nums[nums[i]])

        return value
            
