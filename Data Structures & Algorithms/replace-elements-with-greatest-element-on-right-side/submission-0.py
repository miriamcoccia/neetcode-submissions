class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = arr[:]
        max_value = 0
        for i in range(len(arr) -1, -1, -1):
            result[i] = max_value
            if arr[i] > max_value:
                max_value = arr[i]

        result[-1] = -1
        return result

        

