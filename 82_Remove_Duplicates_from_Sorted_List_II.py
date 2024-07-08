# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        returnHead = ListNode()
        previous = returnHead
        current = head
        stack = []
        while (current != None):
            if stack and current.val != stack[-1].val:
                if len(stack) > 1:
                    stack = []
                else:
                    previous.next = stack.pop()
                    previous = previous.next
            stack.append(current)
            current = current.next

        if len(stack) > 1:
            previous.next = None
        if len(stack) == 1:
            previous.next = stack.pop()

        return returnHead.next
