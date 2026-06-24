class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pns = list(map(lambda p, s: (p, s), position, speed))
        pns.sort()
        stack = []
        for p, s in pns[::-1]:
            stack.append((p,s, (target - p) / s))
            if len(stack) >= 2 and stack[-1][2] <= stack[-2][2]:
                stack.pop()
                
        return len(stack)