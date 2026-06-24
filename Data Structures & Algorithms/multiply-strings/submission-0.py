class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m = len(num1)
        n = len(num2)

        res = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                digit1 = ord(num1[i]) - ord("0")
                digit2 = ord(num2[j]) - ord("0")

                product = digit1 * digit2
                pos = i + j + 1

                total = product + res[pos]

                res[pos] = total % 10
                res[pos - 1] += total // 10

        return "".join(map(str, res)).lstrip("0")