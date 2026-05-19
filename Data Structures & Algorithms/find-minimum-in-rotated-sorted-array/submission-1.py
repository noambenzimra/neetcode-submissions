class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] >nums[r]:
                l = m + 1
            elif nums[m] > nums[l]:
                r = m - 1
            else:
                if m - l > 1:
                    l = l + 1
                if r - m > 1:
                    r = r - 1
                else:
                    return nums[m]
                
        return nums[l]


