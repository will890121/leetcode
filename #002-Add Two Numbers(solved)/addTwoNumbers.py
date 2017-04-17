# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return self.addTwoListNode(None, l1, l2, 0)

    def addTwoListNode(self, nIndex, n1, n2, carry):
        n1Val = n1.val if n1 is not None else 0
        n2Val = n2.val if n2 is not None else 0
        n1Next = n1.next if n1 is not None else None
        n2Next = n2.next if n2 is not None else None
        valSum = n1Val + n2Val + carry
        valMod = valSum % 10
        valCarry = valSum // 10
        if n1 is None and n2 is None:
            return ListNode(carry) if carry > 0 else None
        else:
            nIndex = ListNode(valMod)
            nIndex.next = self.addTwoListNode(nIndex, n1Next, n2Next, valCarry)
        return nIndex


if __name__ == '__main__':
    a = ListNode(0)
    a.next = ListNode(1)
    a.next.next = ListNode(2)
    a.next.next.next = ListNode(3)
    b = ListNode(2)
    b.next = ListNode(3)
    b.next.next = ListNode(4)
    b.next.next.next = ListNode(5)
    print(Solution().addTwoNumbers(a, b))
