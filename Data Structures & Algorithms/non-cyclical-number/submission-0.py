class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def getNext(num):
            total = 0

            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total

        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = getNext(n)
        
        return True