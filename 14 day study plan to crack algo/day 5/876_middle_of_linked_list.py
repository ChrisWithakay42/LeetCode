from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        prev_slow = None

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            prev_slow = slow
            slow = slow.next

        if fast is None:
            return slow
        else:
            return prev_slow.next
