class Solution:
    def countbit(self, n:int) -> int:
        count = 0
        while n:
            if  n % 2 != 0:
                count += 1
            n = n // 2
        return count     
    def countBits(self, n: int) -> List[int]:
        arr = []
        num = 0
        while num <= n:
            ones = self.countbit(num)
            arr.append(ones)
            num = num + 1
        return arr




