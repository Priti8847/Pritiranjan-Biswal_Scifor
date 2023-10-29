##https://leetcode.com/problems/lemonade-change/description/?envType=study-plan-v2&envId=programming-skills
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill_5 = 0  # Number of $5 bills
        bill_10 = 0  # Number of $10 bills

        for bill in bills:
            if bill == 5:
            # If the customer pays with a $5 bill, increment the count of $5 bills.
                bill_5 += 1
            elif bill == 10:
            # If the customer pays with a $10 bill, decrement the count of $5 bills.
            # If there are no available $5 bills, return False.
                if bill_5 <= 0:
                    return False
                bill_5 -= 1
                bill_10 += 1
            elif bill == 20:

            # If the customer pays with a $20 bill, we need to give back $15 in change.
            # First, try to give a $10 bill and a $5 bill as change.
            # If not possible, give three $5 bills as change.
                if bill_10 >= 1 and bill_5 >= 1:
                    bill_10 -= 1
                    bill_5 -= 1
                elif bill_5 >= 3:
                    bill_5 -= 3
                else:
                    return False
            else:
            # If the customer pays with an invalid bill, return False.
                return False

    # If all transactions are successful, return True.
        return True
        
