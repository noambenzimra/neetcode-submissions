import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-x for x in nums]
        heapq.heapify(max_heap)

        for _ in range (k):
            num = -1 *heapq.heappop(max_heap)
        return num

