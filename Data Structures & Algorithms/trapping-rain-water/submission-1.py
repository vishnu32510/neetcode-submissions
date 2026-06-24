class Solution:
    def trap(self, height: List[int]) -> int:
        # Tow Pointer
        if not height:
            return 0
        n = len(height)
        l = 0
        r = n - 1
        maxL, maxR = height[l], height[r]
        res = 0
        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                res += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                res += maxR - height[r]
        return res

        # Brute Force
        # if not height:
        #     return 0

        # n = len(height)
        # res = 0

        # for i in range(n):
        #     leftmax = rightmax = height[i]

        #     for j in range(i):
        #         leftmax = max(leftmax, height[j])
        #     for k in range(i+1, n):
        #         rightmax = max(rightmax, height[k])

        #     res += min(leftmax, rightmax) - height[i]
        # return res