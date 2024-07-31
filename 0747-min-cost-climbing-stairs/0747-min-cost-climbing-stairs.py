class Solution:
    def solve(self, cost, n, dp):
        if n==0:
            return cost[0]
        if n==1:
            return cost[1]
        
        if dp[n]!=-1:
            return dp[n]
        
        ans = min(self.solve(cost,n-1,dp), self.solve(cost,n-2, dp)) + cost[n]
        dp[n]=ans

        return ans

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0]*n
        
        dp[0]=cost[0]
        dp[1]=cost[1]

        for i in range(2,n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])


        return min(dp[n-1], dp[n-2])
        