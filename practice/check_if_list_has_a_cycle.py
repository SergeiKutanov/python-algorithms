visited = {}


class Solution:
    @staticmethod
    def my_solution(head):
        global visited
        if head is None:
            return False
        visited.update({head: None})
        head = head.next
        if head in visited:
            return True
        if head is not None:
            return Solution.has_cycle(head.next)
        return False

    @staticmethod
    def slow_fast_pointers_solution(head):
        fast = head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            head = fast.next
            if head == fast:
                return True
        return False
