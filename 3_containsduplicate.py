class Solution(object):
    def containsDuplicate(self, nums):
        """
        Given an integer array nums, return true if any value appears at least twice in the array, and return false if
        every element is distinct.

        Example 1:

        Input: nums = [1,2,3,1]
        Output: true
        Example 2:

        Input: nums = [1,2,3,4]
        Output: false
        Example 3:

        Input: nums = [1,1,1,3,3,4,3,2,4,2]
        Output: true

        Constraints:
        1 <= nums.length <= 105
        -109 <= nums[i] <= 109
        :type nums: List[int]
        :rtype: bool

        Algorithm:
        First, sort the nums array. Once sorted, any duplicate values will appear next to each other.
        So iterate through nums from index  i = 0 to i = len(nums) - 1 and check if nums[i] == nums[i + 1].
        """
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return bool(True)
        return bool(False)


a = Solution()
nums = [1, 2, 3, 4]
b = a.containsDuplicate(nums)
print(b)  # should print False
