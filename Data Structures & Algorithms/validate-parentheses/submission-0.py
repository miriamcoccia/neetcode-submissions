class Solution:
    def isValid(self, s: str) -> bool:
        sequence = [] 
        # an uneven nr of brackets can't be correctly closed
        if len(s) % 2 != 0:
            return False
        for i in s:
            if i in "[({":  # add the first item to the new sequence
                sequence.append(i)
            if i in "])}":
                if not sequence:
                    return False
                if sequence[-1] == "[" and i == "]":
                    sequence.pop()
                elif sequence[-1] == "(" and i == ")":
                    sequence.pop()
                elif sequence[-1] == "{" and i == "}":
                    sequence.pop()
                else:
                    return False



        if len(sequence) == 0:
            return True
        else:
            return False
            