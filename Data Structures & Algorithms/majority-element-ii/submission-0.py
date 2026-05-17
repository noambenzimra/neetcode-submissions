class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        my_map ={}

        for i in range(len(nums)):
            if nums[i] not in my_map:
                my_map[nums[i]] = 0
            my_map[nums[i]] =  my_map[nums[i]] +1
        res = []
        for key in my_map:
            if my_map[key] > len(nums) // 3:
                res.append(key)
        return res
                