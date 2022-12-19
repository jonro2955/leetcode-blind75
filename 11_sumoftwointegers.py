class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int

        https://leetcode.com/problems/sum-of-two-integers/

        If can't use + operator, a clever workaround in python is to just use the list sum()
        function:

        list=[a,b]
        return sum(list)

        But the goal is use bitwise operators. So to do that, must use bitwise AND OR XOR NOR and
        bit-shifts like << (left) and >> (right). These will convert numbers into binary and do
        bitwise operations on each digits.

        So consider these simple number conversions and the following bitwise ops.
        0 =  00
        1 =  01
        2 =  10
        3 =  11
        4 = 100
        5 = 101
        OR: 2|3 = 3 because if we operate on each bit-pairs, 10|11 => 11
        XOR: 2^3 => 10^11 => 01
        AND: 2&3 => 10&11 => 10
        Bit shift: (2&3) => 10; (2&3)<<1 => 100. Shift to the left by adding a zero at the right.

        So,

        If a = 1,  b = 2, ===> a = 01, b = 10. Need to return binary 3: 11.
        a|b => 11. This works in this case, but,

        If a = 2, b = 3, ===> a = 10, b = 11. Need to return 5 in binary: 101.
        a|b gives 11, the same as in the last example. So that doesn't work. We need 101, not 11.
        Doing a^b => 01 as a preliminary step will be a step in the right direction because it
        gives us the last 2 digits of the desired ans: 101.
        But now we have to get the first digit: a carry of 1.
        That carry is achieved with an AND operation (a&b) combined with a left bit-shift:
        (a&b)<<1 => 100.
        Then we OR the 2 parts together to get the desired ans: 001|100 => 101

        This cannot be easily implemented in python, so first we show it in Java and JS,
        very simple and elegant. Note how the loop will keep carrying if there is something to
        carry. Java:

        public int getSum(int a, int b) {
            int carry;
            while (b != 0) {
                carry = (a & b) << 1;
                a = a ^ b;
                b = carry;
            }
            return a;
        }

        In JS, it is virtually identical:

        var getSum = function(a, b) {
            let carry;
            while(b != 0){
                carry = (a & b) << 1;
                a = a ^ b;
                b = carry;
            }
            return a;
        };

        Stepping through the loop: imagine we have input arguments a = 2 (10), b = 3 (11).
        In the 1st iteration, carry will be 100, a will be 01, b will be 100. In the second
        iteration,
        carry=0, a=101, b=0. Since b=0, the loop stops and we return with a=101. This works.

        Trouble of implementing this algorithm in python:
        In most other languages, integers have fixed lengths like 32 bits. So in the
        while loop, the carry (variable b) will eventually be shifted out of bounds and become 0,
        stopping the while loop.

        But in Python, the number of bits assigned to the integer length is unlimited,
        so this algorithm will go into an infinite loop. So in python you have to bound the
        length of "sum" and "carry" by setting up a mask of
        0xFFFFFFFF. 0xFFFFFFFF is a hexadecimal number. Since F(hex) => 15(decimal) => 1111(
        binary), 0xFFFFFFFF
        means 1111 1111 1111 1111 1111 1111 1111 1111 (32 1-bits in binary). Setting up a
        mask means we AND the sum and carry with this mask, which returns 32 bit integers.

        The masking alone will work for positive input arguments, but for any negative sums,
        masking alone will lose the negative sign. For example, for the case a = -12,
        b=-8. We know the
        answer needs to be -20, and the current code will produce 32 bits 0xFFFFFFEC which will
        be read as -20, in most languages, but Python will believes this is a large
        positive integer 4294967276 because all the bits to the far left are 0. Since Python
        integers have "infinite" length, for it to recognize -20, it needs to see 0x...FFFFFFFFFFFFFFEC
        where there are infinitely many Fs. To convert the 32 bit 0xFFFFFFEC to the infinite bits
        0x...FFFFFFFFFFFFFFEC, we need a conversion called "two's complements": Flip all the
        bits, then add one.

        The actual code to do this madness can be found in
        https://leetcode.com/problems/sum-of-two-integers/solutions/776952/python-best-leetcode-371-explanation-for-python/?orderBy=most_votes

        To sum up, since Python allows arbitary length for integers, we first use a mask
        0xFFFFFFFF to restrict the lengths, and to recover information for negative numbers,
        we use the magical formula ~(a^mask) to convert the result to Python-interpretable form.
        """
        if a == 0:
            return b
        elif b == 0:
            return a

        mask = 0xffffffff

        # in Python, every integer is associated with its two's complement and its sign.
        # However, doing bit operation "& mask" loses the track of sign.
        # Therefore, after the while loop, a is the two's complement of the final result as a
        # 32-bit unsigned integer.
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        # a is negative if the first bit is 1
        if (a >> 31) & 1:
            return ~(a ^ mask)
        else:
            return a

