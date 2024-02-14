class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start, end = 0, 1
        while end < len(nums):
            if nums[start] == 0 and nums[end] != 0:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
            if nums[start] != 0:
                start = end
            end += 1
