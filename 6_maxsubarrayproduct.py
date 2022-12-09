class Solution(object):
    def maxProduct(self, nums):
        """
        https://leetcode.com/problems/maximum-product-subarray/
        :type nums: List[int]
        :rtype: int

        Brute force approach: use 2 nested loops to evaluate the products of all possible
        subarrays, and push them into a new array at each iteration. Return the max value of
        the products array.

        products = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                prod = 1
                for num in nums[i:j+1]:
                    prod *= num
                result.append(prod)
        return max(products)


        The above, however, does not pass LC's time efficiency test. Therefore, the code below
        was obtained from other submissions.
        """

        max_prod = nums[0]
        min_prod = nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            """
            From index 1 to len(nums), evaluate min and max values from a set of 3 numbers:
            1) nums[i] 2) max_prod * nums[i] and 3) min_prod * nums[i]
            2 and 3 are the running min and max products, which despite their names can become 
            higher or lower than the other at each iteration depending on the value of 
            the current nums[i]. We need to keep track of the min values because of the 
            possibility of lower negative numbers producing a larger product. 
            By continuously updating ans to the current max, we arrive at the answer.
            
            [2,3,-2,4]
            x) i=1(3):min(3,6,6)=>3; i=2(-2):min(-2,-12,-6)=>-12; i=3(4):min(4,-8,-48)=>-48
            y) i=1(3):max(3,6,6)=>6; i=2(-2):max(-2,-12,-6)=> -2; i=3(4):max(4,-8,-48)=> 4
            """
            x = min(nums[i], max_prod * nums[i], min_prod * nums[i])
            y = max(nums[i], max_prod * nums[i], min_prod * nums[i])
            min_prod = x
            max_prod = y
            ans = max(max_prod, ans) # ans is also a running max value starting from nums[0]
        return ans
