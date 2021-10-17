class Solution:
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        # Iterate the fast pointer first
        # slow remains the same as head, only fast is being iterated
        for _ in range(n):
            fast = fast.next
        # If reach the end return the next list
        if not fast:
            return head.next
        # Iterate the list until fast reaches the end
        while fast.next:
            fast = fast.next
            slow = slow.next
        # Replace the current position of slow with the .next.next position of slow
        slow.next = slow.next.next
        return head
