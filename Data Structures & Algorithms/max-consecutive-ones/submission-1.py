class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0 
        max_ones = 0  
        for i in nums:
            if i == 1:
                counter += 1
            else:
                counter = 0
            if counter > max_ones:
                    max_ones = counter
            
        return max_ones
