class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Without binary operations (very inefficient, 17%, 28%):

        def missingNumber(self, nums):
            n=len(nums)
            ans=0
            for i in range(n+1):
                if i not in nums:
                    return i


        The proper binary approach using XOR (very efficient, 97%, 88%):

        By this problem, if nums = [0,1,3], we'd need to compare it with indices = [0,1,2,3] and return the missing number, 2.

        XOR'ing a number A twice with B, like A^B^B, will cancel out the B and leave you with A.

        That's because B^B=0, and XOR is commutative, meaning the order of operations order does not matter with XOR.
        Like multiplication, we can rearange the numbers in a series of XORs (regardless of brackets) and the result
        will be the same:

        1^1^2 = (2^1)^1 = (1^1)^2 = 0^2 ===> 00^10 = 10 ===> 2

        Create a series of XORs using each number in nums as well as the set of indices from 0 upto n:

        let numsXor = (0^1^3)
        let indicesXor = (0^1^2^3)
        numsXor^indicesXor = (0^1^3)^(0^1^2^3) = (0^0)^(1^1)^(2)^(3^3) = 0^0^2^0 = 2

        In code, you dont have to create an array of these XOR sequences - you can just XOR a
        successive series of numbers together in a loop:
        """
        sequence = 0
        for i in nums:
            sequence = sequence ^ i
        for i in range(len(nums)):
            sequence = sequence ^ i
            # python remembers the last for-loop index used, even outside the loop
            # XOR the last number n=(i+1) separately, because it is out of range
        sequence = sequence ^ (i + 1)
        return sequence

        """
        alternate form using python enumerate():

        sequence=0
        for i,v in enumerate(nums):
            sequence^=(i^v)
        return sequence^(i+1)
        """