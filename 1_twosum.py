class Solution(object):
    def twosum(self, nums, target):
        """
        https://leetcode.com/problems/two-sum/
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        Algorithm:
        For each index i in nums, iterate through the same list again in a nested loop,
        where index j starts from i+1 so that we don't use the same item twice.
        For each nested loop iteration, if (nums[i] + nums[j] == target), then i anf j are
        the two indices that meets our requirement.
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


a = Solution()
nums = [2, 7, 11, 15]
target = 9
b = a.twosum(nums, target)
print(b)


'''
# alternate form
def twosum(self, nums, target):
    for i in range(len(nums)):
        d = target - nums[i]
        j = nums.index(d)
        if(j != None and i != j):
            return [i, j]
'''