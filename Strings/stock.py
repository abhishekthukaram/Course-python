"""
Best Time to Buy and Sell Stock
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
"""
def maxproft(input):
    max_profit = 0
    min_price = 999999
    for i in range(len(input)):
        if input[i] < min_price:
            min_price = input[i]
        if input[i] - min_price > max_profit:
            print max_profit
            max_profit = input[i]-min_price
    return max_profit


#maxproft([7,1,5,3,6,4])


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit =0
        min_price =99999
        max_profit = 0
        i=0
        while i <len(prices):
            if prices[i] < min_price:
                min_price = prices[i]
                print ("MINIMUM",min_price)
            if prices[i]-min_price >= max_profit:
                max_profit = prices[i]-min_price
                profit+=max_profit
                print (max_profit)
            i+=1
            min_price = 99999
            max_profit =0
        print ("PROFIT",profit)
        return profit


result = Solution()
print result.maxProfit([7,1,5,3,6,4])