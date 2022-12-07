class Solution(object):
    def findMin(self, nums):
        """
        https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
        :type nums: List[int]
        :rtype: int
        Since this is a sorted array and we want a O(log n) algorithm, we can apply binary search.
        But because the array may be rotated, and we're looking for the min value, we need to
        look for the inflection point where next value is decreasing instead of increasing.
        """

        # edge case 1: If list has just one element, return that element
        if len(nums) == 1:
            return nums[0]

        # edge case 2: If last element is greater than first, then there is no rotation
        if nums[len(nums) - 1] > nums[0]:
            return nums[0]

        # binary search on a rotated array - 2 pointers
        left = 0
        right = len(nums) - 1
        while right >= left:
            mid = (left + right) // 2
            """
            If the mid is greater than its next element, that next element is the min.
            Else if the mid is less than its previous element, mid is the min.
            Else if the mid's is greater than the 0th element, this means min is still somewhere 
                in the right half because array is rotated.
            Otherwise, the min is somewhere to the left of mid.
            """
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[0] < nums[mid]:
                left = mid + 1
            else:
                right = mid - 1