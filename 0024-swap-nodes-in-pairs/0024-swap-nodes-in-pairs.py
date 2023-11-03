class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        # Initialize pointers
        dummy = ListNode(0)  # Create a dummy node to simplify edge cases
        dummy.next = head
        prev = dummy
        p = head
        q = head.next

        while p is not None and q is not None:
            # Swap p and q
            prev.next = q
            p.next = q.next
            q.next = p

            # Update pointers for the next iteration
            prev = p
            p = p.next
            if p:
                q = p.next
            else:
                q = None

        return dummy.next  # Return the new head (after the dummy node)
