##https://leetcode.com/problems/repeated-substring-pattern/description/?envType=study-plan-v2&envId=programming-skills
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        data = (s + s)[1:-1]
        return s in data
