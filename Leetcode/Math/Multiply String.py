##https://leetcode.com/problems/multiply-strings/?envType=study-plan-v2&envId=programming-skills
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        int_a=int(num1)
        int_b=int(num2)
        res=int_a*int_b
        return str(res)
        
