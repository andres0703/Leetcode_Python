class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def myPrint(self):
        print(self.val)
        if self.next:
            self.next.myPrint()

# solved in one pass
# use two pointers p1 and p2, both start from the beginning.
# First move p2 n steps, then move p1 and p2 together till p1.next == None.
# At this time p2.next is the one to remove.
class Solution:

    def removeNthFromEnd(self, head, n):
        """
        :param head: ListNode
        :param n: int
        :return: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        p1 = p2 = dummy
        for i in range(n):
            p2 = p2.next
        if p2.next is None:
            return head.next

        while p2.next:
            p2 = p2.next
            p1 = p1.next
        p1.next = p1.next.next
        return head


if __name__ == "__main__":
    h1 = ListNode(1)
    h2 = ListNode(2)
    h3 = ListNode(3)
    h4 = ListNode(4)
    h5 = ListNode(5)
    h1.next = h2
    h2.next = h3
    h3.next = h4
    h4.next = h5

    result = Solution().removeNthFromEnd(h1, 5)
    result.myPrint()
