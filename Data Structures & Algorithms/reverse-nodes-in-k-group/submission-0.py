# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy

        while True:
            # Step 1: check if there are k nodes left
            kth = prev_group_end
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_start = prev_group_end.next
            next_group_start = kth.next

            # Step 2: reverse the k nodes
            prev, curr = next_group_start, group_start
            while curr != next_group_start:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # Step 3: reconnect
            prev_group_end.next = kth
            prev_group_end = group_start
