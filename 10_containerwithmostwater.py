class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int

        Brute force: use nested loops to consider all pairs of lines and calculate the area using
        the lower of the 2 lines and their distance. Put all areas into a list and return the max
        of that list. However, such solutions will never pass the time efficiency test in LC,
        since interviewers expect better.

        Proper approach: Take two pointers, one equal to the starting index and one equal to the
        last index. Maintain a maxarea variable to store the current max area. The height of the
        shorter line dictates the area, and the farther the lines, the more area can be obtained.

        Start considering the area between the two outermost lines, calculate the area, then move
        the pointer at the shorter line inwards. We don't want to move the pointer at the longer
        line inwards since that won't gain any increase in area. The area is dictated by the
        shorter line. A relatively longer line found by moving the shorter line's pointer might
        overcome the reduction in area caused by the width reduction.

        So, while leftPointer < rightPointer, find the area formed between the two pointers to
        update maxarea, move the shorter line inwards, repeat.
        """
        maxarea = 0
        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left
            maxarea = max(maxarea, min(height[left], height[right]) * width)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return maxarea