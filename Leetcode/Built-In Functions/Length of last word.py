##https://leetcode.com/problems/length-of-last-word/description/?envType=study-plan-v2&envId=programming-skills
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
            words=s.split()

            if not words:
                return 0  
    
            return len(words[-1])
