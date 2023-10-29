##https://leetcode.com/problems/largest-perimeter-triangle/description/?envType=study-plan-v2&envId=programming-skills
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)  # Sort in non-decreasing order

        for i in range(len(nums) - 2):
            if nums[i] < nums[i + 1] + nums[i + 2]:
            # If it's possible to form a triangle, return the perimeter
                return nums[i] + nums[i + 1] + nums[i + 2]

    # If no valid triangle is found, return 0
        return 0
        
