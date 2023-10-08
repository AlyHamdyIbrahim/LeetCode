# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        sum = ListNode()
        cur = sum

        carry = 0
        
        while l1 or l2:
            val_l1 = l1.val if l1 else 0
            val_l2 = l2.val if l2 else 0

            cur_sum = (val_l1 + val_l2 + carry) % 10
            carry = (val_l1 + val_l2 + carry) // 10

            cur.next = ListNode(cur_sum)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            cur = cur.next

        if carry:
            cur.next = ListNode(carry)

        return sum.next


# print(Solution().addTwoNumbers([2,4,3], [5,6,4]))

