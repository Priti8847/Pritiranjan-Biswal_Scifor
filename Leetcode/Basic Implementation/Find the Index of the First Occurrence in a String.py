https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/?envType=study-plan-v2&envId=programming-skills
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
         if not needle:
             return 0 

         for i in range(len(haystack) - len(needle) + 1):
             if haystack[i:i+len(needle)] == needle:
                 return i

         return -1 
        
