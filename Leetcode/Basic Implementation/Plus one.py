##https://leetcode.com/problems/plus-one/description/?envType=study-plan-v2&envId=programming-skills
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            sum = digits[i] + carry
            if sum == 10:
                digits[i] = 0
                carry = 1
            else:
                digits[i] = sum
                carry = 0
        if carry == 1:
            digits.insert(0, 1)  
        return digits
