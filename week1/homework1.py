# 167: Two Sum II - Input Array Is Sorted

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0 #left-most index
        right = len(numbers)-1  #right-most index
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left+1, right+1]
            if total > target:
                right -= 1
            else:
                left += 1

# 238: Product of Array Except Self
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        output = [1] * n

        left = 1
        for i in range(n):
            output[i] = left
            left *= nums[i]

        right = 1
        for i in reversed(range(n)):
            output[i] *= right
            right *= nums[i]
        return output

# 75: Sort Colors
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count_0 = 0
        count_1 = 0
        count_2 = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count_0 += 1
            elif nums[i] == 1:
                count_1 += 1
            elif nums[i] == 2:
                count_2 += 1
            i += 1
        for i in range(count_0):
            nums[i] = 0
        for i in range(count_0, count_1+ count_0):
            nums[i] = 1
        for i in range(count_1+count_0, count_2+count_1+count_0):
            nums[i] = 2

