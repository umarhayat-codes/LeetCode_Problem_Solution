class Solution:
    def removeDuplicates(self,head):
        curr = head
        if head is None:
            return head
        else:
            while curr.next is not None:
                if curr.val == curr.next.val:
                    curr.next = curr.next.next
                else:
                    curr = curr.next
            return head
        