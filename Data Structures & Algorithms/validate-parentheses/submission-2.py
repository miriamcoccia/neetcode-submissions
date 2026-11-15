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
            # if the sequence is empty, it means that no opening bracket has been found, thus the parentheses wouldnt have been closed correctly
            # if the opening bracked doesnt match the associated closing bracket - which is the previous item in the sequence
            if not sequence or i != pairs.get(sequence[-1]):
                return False
            else:
                sequence.pop()

        return not sequence
            