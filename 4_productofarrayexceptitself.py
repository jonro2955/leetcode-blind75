class Solution(object):
    def productExceptSelf(self, nums):
        """
        Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the
        elements of nums except nums[i].

        The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

        You must write an algorithm that runs in O(n) time and without using the division operation.

        Example 1:
        Input: nums = [1,2,3,4]
        Output: [24,12,8,6]

        Example 2:
        Input: nums = [-1,1,0,-3,3]
        Output: [0,0,9,0,0]

        Constraints:
        2 <= nums.length <= 105
        -30 <= nums[i] <= 30
        The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
        :type nums: List[int]
        :rtype: List[int]

        Algorithms: https://www.geeksforgeeks.org/a-product-array-puzzle/

        """
        res = [1] * len(nums)  # res => [1 , 1, 1, 1]
        prefix = 1
        postfix = 1

        # input => [1,2,3,4]
        # prefix =>  [1,2,6,24]
        # postfix =>  [24,24,12,4]

        # ans = [1] [1,1,1,1] [1]

        # ans[i] => prefix[i - 1] * postfix[i + 1]
        # ans[0] => prefix[-1] * postfix[1]
        #        => 1 * 24
        #        => [24 , 1 , 1 , 1]
        # ans[1] => [24 , 12 , 8 , 6]

        for i in range(len(nums)):  # [1,2,6,24]
            res[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums) - 1, - 1, - 1):  # [24,24,12,4]
            res[i] *= postfix
            postfix *= nums[i]
        return res


a = Solution()
nums = [1, 2, 3, 4]
b = a.productExceptSelf(nums)
print(b)  # should print [24, 12, 8, 6]

