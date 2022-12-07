class Solution(object):
    def maxProduct(self, nums):
        """
        https://leetcode.com/problems/maximum-product-subarray/
        :type nums: List[int]
        :rtype: int

        Brute force approach: use 2 loops nested to evaluate the products of all possible
        subarrays, and push it into a new array at each iteration. Return the max value of
        the product array.

        result = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                product = 1
                for num in nums[i:j+1]:
                    product *= num
                result.append(product)
        return max(result)


        The above, however, does not pass LC's time efficiency test. Therefore, the code below
        was obtained from other submissions.
        """

        max_prod = nums[0]
        min_prod = nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            # At each iteration from index 1 to len(nums), we need to evaluate the min and max
            # values from a list of 3 numbers:
            # 1) nums[i] 2) max_prod * nums[i] and 3) min_prod * nums[i].
            # Numbers 2 and 3 are the running min and max products, which can become either
            # higher or lower than the other at each iteration depending on the value and
            # signage of nums[i].
            # By continuously updating the ans to the current max_prod, we arrive at the answer.
            x = min(nums[i], max_prod * nums[i], min_prod * nums[i])
            y = max(nums[i], max_prod * nums[i], min_prod * nums[i])
            # [2,3,-2,4]
            min_prod = x  # i1(3):x(3,6,6)=>6; i2(-2):x(-2,-12,-6)=> -2; i3(4):x(4,-8,-48)=> 4
            max_prod = y  # i1(3):y(3,6,6)=>3; i2(-2):y(-2,-12,-6)=>-12; i3(4):y(4,-8,-48)=>-48
            ans = max(max_prod, ans)
        return ans
