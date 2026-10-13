class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            s = str(x)
            rev = s[::-1]
            num = int(rev)
            if num < -2**31 or num > 2**31 - 1:
                return 0

        if x < 0 :
            x = x * -1
            s = str(x)
            rev = s[::-1]
            num = int(rev)
            num = num * -1
            if num < -2**31 or num > 2**31 - 1:
                return 0
    
        if x ==0:
            num =0
        return num        