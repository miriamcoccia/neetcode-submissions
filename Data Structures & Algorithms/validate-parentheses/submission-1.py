class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"[": "]", "(": ")", "{": "}"}
        sequence = [] 
        # an uneven nr of brackets can't be correctly closed
        if len(s) % 2 != 0:
            return False
        for i in s:
            if i in "[({":  # add the first item to the new sequence
                sequence.append(i)
                continue
            if not sequence or pairs.get(sequence[-1]) != i:
                return False
            else:
                sequence.pop()

        return not sequence
            