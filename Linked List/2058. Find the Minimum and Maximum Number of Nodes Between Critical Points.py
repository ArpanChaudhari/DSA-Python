from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        # Need at least 3 nodes
        if head is None or head.next is None or head.next.next is None:
            return [-1, -1]

        min_distance = float("inf")
        max_distance = 0

        first_critical_point = -1
        prev_critical_point = -1

        prev = head
        curr = head.next
        index = 1

        # Traverse until the second-last node
        while curr.next is not None:

            # Check if current node is a critical point
            is_maxima = curr.val > prev.val and curr.val > curr.next.val
            is_minima = curr.val < prev.val and curr.val < curr.next.val

            if is_maxima or is_minima:

                # Store the first critical point
                if first_critical_point == -1:
                    first_critical_point = index

                # Calculate distances if this isn't the first critical point
                if prev_critical_point != -1:
                    min_distance = min(
                        min_distance,
                        index - prev_critical_point
                    )

                    max_distance = index - first_critical_point

                # Update previous critical point
                prev_critical_point = index

            # Move forward
            prev = curr
            curr = curr.next
            index += 1

        # Need at least two critical points
        if min_distance == float("inf"):
            return [-1, -1]

        return [min_distance, max_distance]