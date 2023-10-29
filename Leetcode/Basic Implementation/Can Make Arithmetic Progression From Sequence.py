##https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/description/?envType=study-plan-v2&envId=programming-skills
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        ##first we have to sort the list
        arr.sort()
        for i in range(2,len(arr)):
            if arr[i]-arr[i-1]!= arr[1]-arr[0]:
                return False
        return True
