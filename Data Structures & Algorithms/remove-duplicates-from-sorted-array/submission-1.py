class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insert_idx = 1
        k = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i - 1]:
                k+=1
                nums[insert_idx] = nums[i]
                insert_idx+=1
        return k

                
        





#[2,10,10,30,30,30]
