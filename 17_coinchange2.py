'''
Example 1: Suppose you want to make the sum of 8 cents, what are the total number of coin combinations you can make?
Answer: 2 because,
1st way: 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 = 8 cents.
2nd way: 1 + 1 + 1 + 5 = 8 cents.

Example 2: Suppose this time, the sum is 10 cents. What are the total number of combinations of the coins?
Answer: 4 because,
1st way: 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 = 10 cents.
2nd way: 1 + 1 + 1 + 1 + 1 + 5 = 10 cents.
3rd way: 5 + 5 = 10 cents.
4th way: 10 cents = 10 cents.

How do we programmatically determine the total number of combinations of coins that add to given values of N?

Dynamic Programming: Dynamic programming is a method of simplifying a problem into smaller pieces and incrementally building up the desired output using the results from each successive results. For example, 3 * 89 may not be calculated right away, but if you knew what 3 * 88 was, then you can just add 3 to get the answer. This is the essence of dynamic programming.

Dynamically solving a problem always involves creating a "cache" list of a specific size and iteratively updating each item based on that item's index number according to a "recurrence relation". The iterations will run for a specified number of times as defined by the problem, and at the end, the  last index position will contain the answer.

Let's consider our example: Array of coins: [1, 5, 10], N = 12. We need to determine the number of ways we can make 12 cents out of 1, 5 and 10 cent coins.

First, we create a "cache" array of N + 1 items initialized to 0, where each item will represent the number of ways we can create a sum equalling that item's index number using the current coin, and we will iterate through the array for each coin. We initialize this array like this:

ways:
[0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
indices reference:
[0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12]
The indices reference array simply serves as a visual reference tool for comparing the coins to the index values. It is not used in our algorithm.

The extra addition of 1 in creating our "cache" array of N + 1 items is to account for a special sum: 0. We need to consider the sum of 0 because it provides a base case for our incremental process of building up of each subsequent sums. This base case is ways[ 0 ] = 1 because there is only 1 way to make the sum of 0 cents: by using 0 coins.

ways:
[1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
indices reference:
[0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12]

Now, here is the recurrence relation. We'll take the first coin, the penny, and compare it to each index number i. If the coin is less than or equal to j, then

ways[ i ] becomes ways[ i - coin ] + waysprev[ i ]

This says that the number of ways to make sum = i using the current coin is equal to the number of ways of making sum = ( i - currentCoin ) using the current coin plus the previously computed number of ways of making sum = i using previous coins. If the coin is larger than the index, we leave ways[ i ] alone, as it won't fit. Read on if this doesn't make much sense yet.

Since 1 cent is less than or equal to index values 1 to 12, we add to each of those array items "how many ways the 1 cent coin goes into each index values as the sums, up to the Nth coin". For example, there is 1 way the 1 cent goes into sum = 3: by using three 1-cent coins. For sum = 12, there is also 1 way: twelve 1-cent coins. The same is true for all indices 1-12.

ways:
[1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,   1,   1]
indices reference:
[0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12]

If the recurrence relation doesn't make sense right now, just keep reading. Now let's compare the second coin. Taking the 5 cent nickel and using the same comparison, if the nickel is less than or equal to the index value i, then ways[ i ] becomes ways[ i - coin ] + waysprev[ i ]. Thus we get the following:

ways:
[1,  1,  1,  1,  1,  2,  2,  2,  2,  2,  3,   3,  3]
indices reference:
[0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12]

We are adding how many times the 5 cent coin goes into all of the values leading up the Nth coin. How did we get 3 for index 10? For i = 10, We know that 10 - 5 = 5; so 5 is our
i - coin
And since ways[ 5 ] = 2, adding 2 to waysprev[ 10 ] = 1 equals 3. Therefore, the total number of ways to get the sum of 10 from the coins thus far (using pennies and nickels) is 3.

Lets now compare the third coin, the dimes. The following becomes apparent when we apply the same recurrence relation.

ways:
[1,  1,  1,  1,  1,  2,  2,  2,  2,  2,  4,   4,    4]
indices reference:
[0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  10,  11,  12]

Since we've completed all of our calculations using all the coins, the answer to our example is ways[ N ] = ways[ 12 ] = 4.
'''


class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # Create the ways array to N + 1 to stop the overflow
        ways = [0] * (amount + 1)

        # Set the first way to 1 because there is only 1 way to make 0: with 0 coins
        ways[0] = 1

        # For each coin
        for c in coins:

            # Compare coin to each index value
            for i in range(len(ways)):
                if c <= i:
                    # ways[ j ] becomes ways[ j - coins[ i ] ] + ways[ j ]
                    ways[i] += ways[i - c]

        # Finally, return Nth position item of the Ways array
        return ways[amount]