# 234. Palindrome Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        # slow move one step each time, fast move two steps each time
        # when fast eaches the end, slow is in the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half
        # second half: 2 -> 1 -> Null 
        prev, curr = None, slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        second = prev # second half: Null -> 1 -> 2

        # compare first and second half
        first = head
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True


# 143. Reorder List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, curr = None, slow.next
        slow.next = None # cut the list and reverse second half
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        second = prev # new head of reversed half

        first = head
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            # first move to next, second move to next
            first, second = tmp1, tmp2



# 73: Set Matrix Zeros
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # m * n size matrix
        m, n = len(matrix), len(matrix[0])
        # use set() because we only care which rows and columns contain at least one zero
        # if another zero appears in the same row or column, already marked, does not change the result
        row, column = set(), set()
        # find places where zero occurs
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row.add(i)
                    column.add(j)
        # replace each row with zero
        for i in row:
            for j in range(n):
                matrix[i][j] = 0
        # replace each column with zero
        for j in column:
            for i in range(m):
                matrix[i][j] = 0
