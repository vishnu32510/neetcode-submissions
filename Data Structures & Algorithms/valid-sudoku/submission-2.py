class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if (board[i][j] in rows[i] 
                or board[i][j] in columns[j] 
                or board[i][j] in squares[(i // 3, j // 3)]):
                    return False

                rows[i].add(board[i][j])
                columns[j].add(board[i][j])
                squares[(i // 3, j // 3)].add(board[i][j])
        return True
        
        # # Column
        # for i in range(9):
        #     seen = set()
        #     for j in range(9):
        #         if board[i][j] != '.':
        #             if board[i][j] not in seen:
        #                 seen.add(board[i][j])
        #             else:
        #                 return False
        # # Row
        # for i in range(9):
        #     seen = set()
        #     for j in range(9):
        #         if board[j][i] != '.':
        #             if board[j][i] not in seen:
        #                 seen.add(board[j][i])
        #             else:
        #                 return False

        # #Box
        # for i in range(0,9, 3):
        #     for j in range(0,9, 3):
        #         seen = set()
        #         for k in range(3):
        #             for l in range(3):
        #                 if board[i+k][j+l] != '.':
        #                     if board[i+k][j+l] not in seen:
        #                         seen.add(board[i+k][j+l])
        #                     else:
        #                         return False
        # return True
