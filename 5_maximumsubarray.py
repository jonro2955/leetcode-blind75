class Solution(object):
    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)

        """
        https://leetcode.com/problems/maximum-subarray/
        :type nums: List[int]
        :rtype: int

        Need to evaluate all possible subsets, calculate their sums and find the max among them.

        The subsets themselves aren't important. Their sums are. Even though the problem says 
        find 'subarray', it tells you to return a single sum. So it is more productive to focus on
        the return value rather than fixate on a subarrray.

        Algorithm:

        "Go through each item in the list, and only if the item before it is greater than 0,
        then change the current item to be the sum of it and its preceding item."
        
        This makes each number in the array become the sum of the subset before it that produces an 
        increase in value. 

        If a preceding number is negative, adding it will decrease the value of the current 
        subarray sum, so we need to ignore that to keep the higher sum.
        
        After all iterations are complete, pick the maximum value from the array and 
        return it"

        This solution covers cases where all array values are negative. In such cases, there are
        no subarrays to sum up because any subarray will produce an even lower sum than the
        array values themselves. So we can just pick the max among the negative values.

        In these types of questions where you are trying to find a continuous subset's sum (or
        product) that evauates to the highest value among all possible subsets, the general
        rule is that only those numbers greater than 0 that precedes each number will
        increase the subset's sum (or >1 in the case of a product) so only in those cases you should
        combine the preceding subset with the current array item to evaluate a larger subset
        sum/product. If the preceding value will decrease the current subset's evaluation, then the
        current item becomes the start of a new subset to consider.

        [-2, 1,-3, 4,-1, 2, 1,-5, 4] =>
        [-2, 1,-2, 4, 3, 5, 6, 1, 5] => The max, 6, is the sum of subset [4,-1, 2, 1]

        In code, we cannot evaluate the preceding item of the first item of the array,
        so we start with the second item at index 1.
        """




