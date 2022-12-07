class Solution(object):
    def findMin(self, nums):
        """
        https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
        :type nums: List[int]
        :rtype: int
        Binary search: Since this is a sorted array, we can apply binary search, which is O(log
        n). But because the array can be rotated, and we're looking for the min value,
        instead of looking for an equality match, we need to look for the inflection point where
        next value is decreasing instead of increasing.
        """

        # edge case 1: if the list has just one element, just return that element
        if len(nums) == 1:
            return nums[0]

        # edge case 2: If the last element is greater than the first element, then there is no
        # rotation
        if nums[len(nums) - 1] > nums[0]:
            return nums[0]

        # binary search

        # left pointer
        left = 0
        # right pointer
        right = len(nums) - 1

        while right >= left:
            mid = left + (right - left) // 2
            # if mid is greater than its next element, that next element is the min
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            # if mid is less than its previous element, mid is the min
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            # else: remember we've got a rotated array here. if mid's value is greater than
            # the 0th element, this means min is still somewhere to the right
            if nums[0] < nums[mid]:
                left = mid + 1
            # otherwise, the smallest value is somewhere to the left
            else:
                right = mid - 1