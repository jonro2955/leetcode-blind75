class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        https://leetcode.com/problems/counting-bits/

        Use the algorithm from the "Number of 1 Bits" problem
        (https://leetcode.com/problems/number-of-1-bits/) to
        count the number of 1-bits of each index number.
        """
        ans=[]
        for i in range(0, n+1):
            count = 0
            x=i
            while x != 0:
                count = count + (x & 1)
                x = x>>1
            ans.append(count)
        return ans