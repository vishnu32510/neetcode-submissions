class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        wl = len(word)
        res = [False]
        sol = []
        m = len(board)
        n = len(board[0])
        visited = [[False] * n for _ in range(m)]

        def backtrack(i, j):
            if res[0]:
                return
            if len(sol) == wl:
                if "".join(sol) == word:
                    res[0] = True
                return
            if i >= m or j >= n or i < 0 or j < 0:
                return
            if visited[i][j]:
                return
            
            visited[i][j] = True
            sol.append(board[i][j])
            backtrack(i + 1, j)

            backtrack(i, j + 1)

            backtrack(i - 1, j)

            backtrack(i, j - 1)

            sol.pop()
            visited[i][j] = False

        for i in range(m):
            for j in range(n):
                backtrack(i,j)
        return res[0]