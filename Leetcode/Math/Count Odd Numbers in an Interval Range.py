##https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/description/?envType=study-plan-v2&envId=programming-skills
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count=0
        for i in range(low,high+1):
            if i%2!=0:
                count+=1
        return count
        
        
        
