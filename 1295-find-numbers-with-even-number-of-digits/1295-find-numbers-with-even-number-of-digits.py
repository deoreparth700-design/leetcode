class Solution(object):
    def findNumbers(self, nums):
        even_number = 0

        for num in nums:
            digit_count = 0

            while num > 0:
                digit_count += 1
                num = num // 10

            if digit_count % 2 == 0:
                even_number += 1

        return even_number
        