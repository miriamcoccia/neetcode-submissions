class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i in range(len(operations)):
            if operations[i] == "+":
                last_val = record[-1]
                prev_val = record[-2]
                record.append(last_val + prev_val)
            elif operations[i] == "C":
                record.pop()
            elif operations[i] == "D":
                record.append(record[-1] * 2)
            else:
                record.append(int(operations[i]))
        return sum(record)
