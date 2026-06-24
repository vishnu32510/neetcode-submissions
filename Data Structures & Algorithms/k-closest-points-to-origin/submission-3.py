class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pointsOrder = []

        heapq.heapify(pointsOrder)

        for point in points:
            x, y = point
            distance = x**2 + y**2
            heapq.heappush(pointsOrder, (distance, point))

        ans = []
        while k > 0:
            dist, (x,y) = heapq.heappop(pointsOrder)
            ans.append([x, y])
            k -= 1
        return ans