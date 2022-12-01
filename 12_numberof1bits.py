class Solution(object):
    def hammingWeight(self, n):
        """
        https://leetcode.com/problems/number-of-1-bits
        :type n: int, equal to a binary string representation of a number
        :rtype: int
        """
        count = 0
        for char in str(bin(n)):
            if char == "1":
                count += 1

        return count


"""
Shorthand option using python's built in count() function:

    def hammingWeight(self, n):
        return str(bin(n)).count("1")

"""

