class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1

        while l <= r:
            m = (l + r) // 2

            if self.time(piles , m) > h:
                l = m + 1
            elif self.time(piles , m) <= h :
                r = m - 1        
        return l 

    def time(self, piles: List[int],freq: int) ->int:
        time = 0
        for pile in piles:
            if freq > pile:
                time+=1
            else :
                left_time = pile//freq
                if pile%freq > 0 :
                    left_time +=1
                time = time + left_time
            
        return time