class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # for num2 in nums2:
        #     nums1[m] = num2
        #     m+=1
        
        # return nums1.sort()

        j, i = n-1, m-1
        last = m + n - 1

        while j >= 0 and i >= 0:
            print(j)
            if nums2[j] < nums1[i]:
                nums1[last] = nums1[i]
                i-=1
            else:
                nums1[last] = nums2[j]
                j-=1
            last-=1
        
        while last >= 0 and j >= 0 : 
            nums1[last] = nums2[j]
            last-=1
            j-=1

        return nums1

        # [10,20,20,40,60,0,0]i, [1,30]j

