# Methode 1

class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        

        while n != 1 and n not in visit:
            visit.add(n)
            res = 0
            while n:
                digit = n % 10
                res += digit * digit
                n = n // 10
            
            n = res
        return n == 1
                
                