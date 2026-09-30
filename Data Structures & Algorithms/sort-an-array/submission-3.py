class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(left, right):
            result = []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i+=1
                else:
                    result.append(right[j])
                    j+=1
            while i < len(left):
                result.append(left[i])
                i+=1
            while j < len(right):
                result.append(right[j])
                j+=1
            return result            
        def mergeSort(arr):
            if len(arr) <= 1:                    # תנאי עצירה: 0 או 1 איברים = ממוין
                return arr
            mid = len(arr) // 2
            left = mergeSort(arr[:mid])          # חוזר ממוין
            right = mergeSort(arr[mid:])         # חוזר ממוין
            return merge(left, right)            # מאחדים שתי רשימות ממוינות

        return mergeSort(nums)
