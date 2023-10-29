##https://leetcode.com/problems/robot-return-to-origin/description/?envType=study-plan-v2&envId=programming-skills
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        a=0
        b=0
        c=0
        d=0
        for i in moves:
            if i=='U':
                a+=1
            elif i=='D':
                b-=1
            elif i=='L':
                c+=1
            elif i=='R':
                d-=1
        e=a+b
        f=c+d
        if e==0 and f==0:
            return True
        return False
        
