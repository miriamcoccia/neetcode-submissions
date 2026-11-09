class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        max_ones = 0
        for n in nums:
            if n == 1:
                counter += 1
            else:
                counter = 0
            max_ones = max(max_ones, counter)
        return max_ones