class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = i + 1
        print(nums[i])
        for n in nums: 
            while i != j and j <= len(nums) - 1:
                if nums[i] + nums[j] == target:
                    return [i, j]
                j += 1
            i += 1
            j = i + 1
        return [i, j]