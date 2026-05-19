class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cur_sum = target
        min_sub = float("inf")
        cur_sub = 0
        l = 0
        for r in range(len(nums)):
            cur_sum -= nums[r]
            cur_sub +=1
            while cur_sum <= 0:
                  min_sub = min(min_sub,(r-l) + 1)
                  cur_sum += nums[l]
                  l = l+1
                  cur_sub -=1
        return 0 if min_sub == float("inf") else min_sub

