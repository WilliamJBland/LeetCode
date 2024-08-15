"""
Given a string s, return the longest palindromic substring in s.
"""
import heapq


class MedianFinder:

    def __init__(self):
        self.max_heap, self.min_heap = [], []

    def addNum(self, num: int) -> None:

        heapq.heappush(self.min_heap, num * -1)
        if len(self.min_heap) == 1 and not self.max_heap:
            return
        if self.max_heap and (self.min_heap[0] * -1) > self.max_heap[0]:
            heapq.heappush(self.max_heap, heapq.heappop(self.min_heap)* -1)

        dif = len(self.min_heap) - len(self.max_heap)
        if dif > 1:
            heapq.heappush(self.max_heap, heapq.heappop(self.min_heap) * -1)
        elif dif < -1:
            heapq.heappush(self.min_heap, heapq.heappop(self.max_heap) * -1)

    def findMedian(self) -> float:
        if (len(self.max_heap) + len(self.min_heap)) % 2 == 0:
            return (self.min_heap[0] * -1 + self.max_heap[0]) / 2
        else:
            return self.min_heap[0] * -1 if len(self.min_heap) > len(self.max_heap) else self.max_heap[0]
