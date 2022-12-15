class Solution(object):
	def hammingWeight(self, n):
		"""
		:type n: int
		:rtype: int

		Simple solution without using binary operations:

		count=0
		for char in str(bin(n)):
			if char=="1":
				count+=1
		return count

		Shorthand of above:

		return str(bin(n)).count("1")

		But the goal is to use binary operators, so we can use bitwise shift operators with AND
		1's. The idea is that when we do
		an AND operation on a number x with the number 1 as the other operand, as in x&1, the result will be 1 if and only
		if the last binary digit of x is 1. I.e. 1011 & 1 = 1; 1010 & 1 = 0; because 1 = 0001. Using this, we can check if
		the last binary digit of n is 1. Then, we can do a bitwise right-shift of n to check the same on the second-last
		binary digit of n. Repeat this len(n) times to check all digits.
		"""
		count = 0
		while n != 0:
			count = count + (n & 1)
			n = n>>1
		return count

