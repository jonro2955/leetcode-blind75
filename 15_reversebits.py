class Solution:
    """
    @param n, an integer
    @return an integer

    Technique: ANDing a number n with 1, as in (n & 1), returns the last bit of n.
    Ex: If n=101, then 101 & 1 = 1 because 101 & 001 = 001.

    In a loop, we can continually get the last bit, shift n to the right (n=n>>1) to delete
    the last bit, then get the last bit again to get the second last bit and so on to get each bit
    of n from right to left. At each iteration, we can append the last bit to another container in
    reverse order.

    Appending it to a container in reverse order involves setting up a variable ans = 0,
    then doing a
    bitwise OR with each bit of n, then left-shift ans to the left by one digit (ans<<=1).
    """

    def reverseBits(self, n):
        ans = 0
        for i in range(32):
            ans = (ans << 1) | (n & 1)
            n >>= 1
        return ans
