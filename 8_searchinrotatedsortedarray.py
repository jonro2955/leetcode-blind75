class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

        Step 1
        If the array is rotated, do a binary search to find the pivot using the same algorithm as
        in problem #7 of blind 75. Then sort the array to un-rotate the array.

        Step 2
        Do a 2nd binary search on the sorted, un-rotated array. This time we are looking for the
        target, not a pivot. Since we know our pivot, we just need to modify our return
        target index value like so: realIndex = (targetIndex + pivot) % nums.Length

        Complexity of 2 binary searches is O ( 2 Log (n)) which is O (Log(n))
        """

        ans = -1
        pivot = 0
        left = 0
        right = len(nums) - 1

        # edge case 1: If list has just one element, return 0 or -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return ans

        # If last element is less than the first, rotation is confirmed. Find the pivot and then sort the array
        if nums[len(nums) - 1] < nums[0]:
            while right >= left:
                mid = (left + right) // 2
                if nums[mid - 1] > nums[mid]:
                    pivot = mid  # set pivot
                if mid < (len(nums) - 1):  # Extra condition to prevent index out of range
                    if nums[mid] > nums[mid + 1]:
                        pivot = mid + 1  # set pivot
                if nums[0] < nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            nums.sort()  # sort

        left = 0
        right = len(nums) - 1
        while right >= left:
            mid = (left + right) // 2
            if nums[mid] == target:
                ans = mid  # Target found. Set the ans.
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        if ans == -1:
            return ans
        else:
            return (ans + pivot) % len(nums)








