##https://leetcode.com/problems/richest-customer-wealth/?envType=study-plan-v2&envId=programming-skills
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth=0
        for money in accounts:
            max_wealth=max(max_wealth,sum(money))
        return max_wealth        
