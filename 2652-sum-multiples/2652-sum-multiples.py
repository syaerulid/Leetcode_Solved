class Solution:
    def sumOfMultiples(self, n: int) -> int:
        self.n = n
        total_sum = 0
        for number in range(n+1):
            if number % 3 == 0:
                total_sum += number
            elif number % 5 == 0:
                total_sum += number
            elif number % 7 == 0:
                total_sum += number
        return total_sum

                