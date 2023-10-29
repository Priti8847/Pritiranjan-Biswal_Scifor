##https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=programming-skills
lass Solution:
    def moveZeroes(self, nums: List[int]) -> None:
         non_zero_index = 0 

   
         for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[non_zero_index] = nums[non_zero_index], nums[i]
                non_zero_index += 1
