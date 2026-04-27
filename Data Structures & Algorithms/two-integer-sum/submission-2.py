class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_numbers = {}
        for i, num in enumerate(nums):
            needed_num = target - num
            if needed_num in seen_numbers :
                return [seen_numbers[needed_num],i]
            seen_numbers[num] = i
        return []
