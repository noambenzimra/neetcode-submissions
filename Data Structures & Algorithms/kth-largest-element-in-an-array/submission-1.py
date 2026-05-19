import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # min_heap = [-x for x in nums]
        # heapq.heapify(max_heap)

        # for _ in range (k):
        #     num = -1 *heapq.heappop(max_heap)
        # return num

        min_heap = []

        for num in nums:
            heapq.heappush(min_heap,num)

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]
