class Solution:
    def reverse(self, x: int) -> int:
        
        sign = 1 if (x >= 0) else -1
        x = list(str(abs(x)))
        x = list(int(i) for i in x)

        l, r = 0, len(x) - 1

        while l < r:
            x[l], x[r] = x[r], x[l]
            l += 1
            r -= 1

        
        num = 0

        for i in range(len(x)):
            num += x[i] * (10 ** (len(x) - i - 1))

        if num > 2**31 - 1 or num < -2**31:
            return 0


  


        return num * sign

            

        



