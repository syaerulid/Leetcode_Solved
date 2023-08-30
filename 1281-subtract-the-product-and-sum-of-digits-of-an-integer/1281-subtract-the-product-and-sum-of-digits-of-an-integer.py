class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_total = 0
        multiply_total = 1

        # change number to list
        string_n = str(n)
        list_n = list(map(int, string_n))

        # perulangan
        for num in list_n:
            sum_total += num
            multiply_total *= num

        output = multiply_total - sum_total
        return output