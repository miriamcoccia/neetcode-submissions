class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0 # writing position, where the first good value should go (beginning)
        for n in nums:
            if n != val: 
                nums[i] = n
                i += 1
        return i

        
        