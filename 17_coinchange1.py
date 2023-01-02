''' https://leetcode.com/problems/coin-change/
Example 1: Suppose coins = [2], and you want to make the sum of N = 3 cents. What are the total
number of coin combinations you can make?
Answer is -1 because we cannot make a sum of 3 cents using only coins of 2 cent denominations.
There is no answer, so we return -1.

Example 2: coins = [1], N = 0.
Answer is 0 because if the required sum is 0, there is 0 ways of creating that sum with any coin.

Example 3: coins = [1,2,5], N = 11.
Answer is 3 because 5 + 5 + 1 = 11. 2 nickels and a penny results in the fewest coins to make 11
cents. Using the largest denominations early and as many times as possible will usually result
in the fewest number of coins, but not always. This approach is called "greedy", and it means
you read all of the array items beforehand and pick the biggest one first and as many times as
possible then move on to the next largest and so on, instead of going from
left to right in order.

But why doesn't the greedy algorithm work all the time?
Suppose coins = [ 1, 3, 4, 5 ] and N = 7. The greedy approach dictates that we use 5 cents
first, so it will force us to use 3 coins: 5 + 1 + 1. However, we could have used only 2 coins:
3 + 4.

(Other approaches such as top-down DFS trees or exhaustive combination searching is way too
inefficient because it creates many repeated computations, as shown by neetcode's video on this
problem https://www.youtube.com/watch?v=H9bfqozjoqs. Dynamic programming provides a "bottom-up"
approach that will efficiently calculate our answer.)

So, dynamic programming step through: Suppose coins = [ 1, 3, 4, 5 ] and N = 7. This has a
similar structure and a different recurrence relation to the problem of coin change 2.

Again, we must create a cache array of size N + 1, but this time, we'll call it min_ways[ ].
Each value of min_ways[ ] will represent the minimum number of coins needed to make the sum
equaling that item's index number using all of the coins available. And instead of initializing
it to all 0s at first, we will initialize it to the maximum of N + 1.

The reason why we initialize each value of min_ways array to N + 1 is because we want the
initial values to be something greater than the greatest possible minimum number of coins needed
to make N. That way, we can return -1 if min_ways[ N ] is greater than N.

If our coin inventory included only a 1 cent coin, then N is the minimum number of coins needed
to make N cents. Since N + 1 is larger than that, so we can use the minimum of the two numbers.
If the initial value was smaller than N, that would cause problems if the actual minimum value
was greater. Read on.

Recurrence relation:
For each index i, we iterate through each coin c, and update min_ways[i] to the smaller of
min_ways[i] and 1 + min_ways[i - c]

Like before, we need a base case when the index/sum, is 0. To make a sum of 0, we need exactly
0 coins. So set the first item to 0:
min_ways[ 0 ] = 0
Now let's think for a moment. What is min_ways[ 1 ]? Well, to make a sum of 1 cent, we can just
use the penny in our coins inventory once:
min_ways[ 1 ] = 1
What about min_ways[ 2 ]? Well, we don't have a 2-cent coin, so the largest coin that fits is
still the penny. So suppose we use one penny. We get a remainder of 1 cent, so we can just add
the previous calculation:
min_ways[ 2 ] = 1 + min_ways[ 1 ] = 1 + 1 = 2
For  min_ways[ 3 ], we have a 3-cent coin that fits, so we just use that once:
min_ways[ 3 ] = 1
The same is true for min_ways[ 4 ] and min_ways[ 5 ]. We have coin denominations that fits both
of those sums in one go:
min_ways[ 4 ] = 1
min_ways[ 5 ] = 1
But for min_ways[ 6 ], what can we do? In this case, all the coins fit incompletely. We can try
iteratively fitting each coin in our inventory once:
    1. Start with a one-cent coin. Then we have to make up 5 cents:
min_ways[ 6 ] = 1 + min_ways[ 5 ] = 1 + 1 = 2
    2. Start with a three-cent coin. Then we have to make up 3 cents:
min_ways[ 6 ] = 1 + min_ways[ 3 ] = 1 + 1 = 2
    3. Start with a four-cent coin. Then we have to make up 2 cents:
min_ways[ 6 ] = 1 + min_ways[ 2 ] = 1 + 2 = 3
    4. Start with a five-cent coin. Then we have to make up 1 cents:
min_ways[ 6 ] = 1 + min_ways[ 1 ] = 1 + 1 = 2
At each iteration, we can keep a running count of the lowest result. At the first iteration,
we set it to the initial result of 2. Then, since it doesn't get any smaller than 2,
we just return 2 as the answer.
min_ways[ 6 ] = 2
The actual composition of the coins does not matter. We just need to evaluate all fitments and
pick the lowest result.
The same goes for min_ways[ 7 ]. All coins in our inventory will fit, so:
    1. Start with a one-cent coin. Then we have to make up 6 cents:
min_ways[ 7 ] = 1 + min_ways[ 6 ] = 1 + 2 = 3
    2. Start with a three-cent coin. Then we have to make up 4 cents:
min_ways[ 7 ] = 1 + min_ways[ 4 ] = 1 + 2 = 2
    3. Start with a four-cent coin. Then we have to make up 3 cents:
min_ways[ 7 ] = 1 + min_ways[ 3 ] = 1 + 1 = 2
    4. Start with a five-cent coin. Then we have to make up 2 cents:
min_ways[ 7 ] = 1 + min_ways[ 2 ] = 1 + 1 = 3
The lowest result was 2 from using 3 and 4 cent denominations once each (and the reverse order
of the same coins) so,
min_ways[ 7 ] = 2
'''

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        # initialize all items as some number larger than amount
        min_ways = [amount + 1] * (amount + 1)

        # set the first way to 0 because there is no way to make 0 cents
        min_ways[0] = 0

        # for each index 1 upto amount
        for i in range(1, amount + 1):

            # for each coin c
            for c in coins:

                if c <= i:
                    min_ways[i] = min(min_ways[i], 1 + min_ways[i - c])

        if min_ways[amount] == amount + 1:
            return -1
        return min_ways[amount]
