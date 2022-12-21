class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int

        https://leetcode.com/problems/climbing-stairs/

        Intuition:

        If there is 1 step remaining, you can only take 1 step, so return 1.
        If there are 2 steps remaining, you can take 1 or 2 steps, so return 2.
        If n>2, separate n into 2 and n-2 steps and add them up.

        if n==1:
            return 1
        if n==2:
            return 2
        return self.climbStairs(n-1)+self.climbStairs(n-2)

        However, a simple recursive solution like above will result in time limit exceeded because
        it recalculates the same values multiple times (see
        https://leetcode.com/problems/climbing-stairs/solutions/1792723/python-in-depth
        -walkthrough-explanation-dp-top-down-bottom-up/).

        Instead, use dynamic programming (save each successive result and incrementally build the
        result from the last calculation).
        Create an array "dp" of length n+1 to accomodate for the 0-based indexing of Python. And
        at each index position,
        insert the number of steps possible as a sum of the last 2 calculations:
        """
        if n == 1 or n == 2:
            return n
        dp = [-1] * (n + 1)  # creates a list of size n+1 filled with all -1
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
