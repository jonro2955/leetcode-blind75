class Solution(object):
    """
    https://leetcode.com/problems/maximum-subarray/

    Given an integer array/list nums, find the subarray which has the largest sum and return its
    sum.

    Example Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.

    Example Input: nums = [1]
    Output: 1

    Example Input: nums = [5,4,-1,7,8]
    Output: 23

    Constraints:
    1 <= nums.length <= 105
    -104 <= nums[i] <= 104

    Note:
    If you have figured out the O(n) solution, try coding another solution using the divide and
    conquer approach.
    """
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

