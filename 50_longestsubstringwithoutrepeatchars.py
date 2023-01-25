class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        https://leetcode.com/problems/longest-substring-without-repeating-characters/
        :type s: str
        :rtype: int

        "sliding window" problem
        Build a set of unique chars as you loop thru the string
        If there is a duplicate, start removing values from the left
        If no duplicates, keep adding to the set and updating the max length of unique chars
        """

        # initialize a python set (a collection with no duplicates) to hold the substring
        subset = set()
        # left pointer is here, right pointer is the index inside the for loop
        left = 0
        answer = 0
        for right in range(len(s)):
            # if the char we are looping thru exists in the subset,
            # keep removing the char from the left sidebased until no duplicates are found
            # "abcabcbb"
            while s[right] in subset:
                subset.remove(s[left])
                left += 1
            # if the char we are looping thru doesn't exist in the subset,
            # add it to the subset and update the answer to the maximum subset length encountered
            subset.add(s[right])
            answer = max(answer, right - left + 1)
        return answer







