class Solution:
    def __init__(self):
        self.operations = []
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        self.operations = operations
        result = 0
        for operation in operations:
            if operation == "X++":
                result += 1
            elif operation == "++X":
                result += 1
            else:
                result -= 1

        return result