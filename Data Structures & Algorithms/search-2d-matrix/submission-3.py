class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        # Binary Search
        left = 0
        right = m * n - 1

        while left <= right:
            mid = (left + right) // 2
            row = mid // n
            col = mid % n
            mid_val = matrix[row][col]

            if mid_val == target:
                return True
            elif target > mid_val:
                left = mid + 1
            else:
                right = mid - 1
        return False

        #Staircase search
        r = 0
        c = n - 1

        while r < m and c >= 0:
            if matrix[r][c] == target:
                return True
            elif target > matrix[r][c]:
                r += 1
            else:
                c -= 1
        return False

        # Brute Force
        # for i in range(m):
        #     for j in range(n):
        #         if target == matrix[i][j]:
        #             return True

        # return False