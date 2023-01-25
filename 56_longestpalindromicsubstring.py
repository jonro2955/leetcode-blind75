class Solution(object):
    def longestPalindrome(self, s):
        """
        Dynamic Programming

        Let P(x,y) stand for palindrome checker that returns true if the substring
        s[x : y + 1] is a palindrome. P can be defined by the following 2 base cases:

        Base case 1:
        P(i, i) = true;
        Because all single character substrings are palindromes by default.

        Base case 2:
        P(i, i + 1) = s[i] == s[i+1];
        Because all two consecutively positioned equal characters constitutes a palindrome.

        Recurrence relation:
        P(i, j) == s[i] == s[j] && P(i + 1, j - 1)
        "For 2 indices i and j, P(i, j) is true if both s[i] and s[j] are equal
        characters and their inner substring  is also a palindrome."


        DP Process:

        1. Set the return value ans initially to s[0], since each single character by
        themselves is a palindrome.

        2. Create a 2D array of size n by n called dp with all cells initialized to False.
        A cell dp[i][j] will become 'True' if a substring from index i to j is a palindrome.

        3. Since each single characters by themselves is a palindrome by default, set
        dp[i][i] = True
        for every i from 0 to n-1.

        4. We process each string character s[i], i in range(n - 1, 0, -1) from right to left,
        and for each i, run a nested loop to process the characters s[j], j in range(i + 1, n - 1)
        rightwards. If s[i] and s[j] are identical neighbours OR if they are identical
        chars whose inner susbtring is a palindrome, then the substring from s[i] to s[j]
        is a palindrome, so we set dp[i][j] to True.

        5. Every time a new palindrome of larger lengths are found, update
        ans to ans = s[i : j + 1]

        Time Complexity - O(N^2), Space Complexity - O(N^2) (caching all substring)
        """

        # 1
        ans = s[0]
        # 2
        dp = [[0] * len(s) for _ in range(len(s))]
        # 3
        for i in range(len(s)):
            dp[i][i] = True
        # 4
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    if j - i == 1 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        # 5
                        if len(s[i: j + 1]) > len(ans):
                            ans = s[i: j + 1]
        return ans


