class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        second_str = {}
        # need to store which letters and how often they show up
        for l in s:
            if l not in letters.keys():
                letters[l] = 1
            else: 
                letters[l] += 1

        for ss in t:
            if ss not in second_str.keys():
                second_str[ss] = 1
            else: 
                second_str[ss] += 1
        if letters == second_str:
            return True
        else:
            return False
        

        