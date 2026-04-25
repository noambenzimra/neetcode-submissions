class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         seen.remove(num)
        #     else:
        #         seen.add(num)
        # return list(seen)[0]
        #that's working but its O(N) in space and not O(1)

        res = 0

        for num in nums:
            res = res ^ num
        return res


