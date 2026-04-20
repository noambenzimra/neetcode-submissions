class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        best_sum = 0
        for i in range (len(prices)):
            if prices[i] < prices[l]:
                l = i
            else:
                best_sum = max(best_sum, prices[i] - prices[l])
        return best_sum
