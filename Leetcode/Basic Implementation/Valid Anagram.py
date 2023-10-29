##https://leetcode.com/problems/valid-anagram/description/?envType=study-plan-v2&envId=programming-skills
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sort_s=sorted(s)
        sort_t=sorted(t)

        if sort_s == sort_t:
            return True
        else:
            return False
