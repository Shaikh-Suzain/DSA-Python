class Solution(object):
    def singleNumber(self, nums):
        for i in nums:                  # <-- typo here
            if nums.count(i) == 1:   # <-- same typo
                return i


class Solution(object):
    def singleNumber(self, nums):
        solution=0
        for num in nums:
            solution ^= num
        return solution

        