class Solution(object):
    def runningSum(self, nums):
        addition = []
        total = 0

        for num in nums:
            total = total + num
            addition.append(total)

        return addition