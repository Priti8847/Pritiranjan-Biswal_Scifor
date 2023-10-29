##https://leetcode.com/problems/add-binary/?envType=study-plan-v2&envId=programming-skills
class Solution:
    def addBinary(self, a: str, b: str) -> str:
         # Convert binary string 'a'and 'b to an integer.
        int_a = int(a, 2)
        int_b = int(b, 2)
        
        # Calculate the sum of the two integers.
        sum_int = int_a + int_b
        
        # Convert the sum back to a binary string.
        binary_sum = bin(sum_int)
        
        # Remove the '0b' prefix from the binary string.
        binary_sum_str = binary_sum[2:]
        
        # Return the binary sum as a string.
        return binary_sum_str
        
