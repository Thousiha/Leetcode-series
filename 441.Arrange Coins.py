class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n<=1:
            return 1
        row=0
        count=0
        for i in range(1,n):
            c= 1*i
            count+=c
            row+=1
            if count>n:
                return row-1
        return row
