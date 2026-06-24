class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Column
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] not in seen:
                        seen.add(board[i][j])
                    else:
                        return False
        # Row
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] != '.':
                    if board[j][i] not in seen:
                        seen.add(board[j][i])
                    else:
                        return False

        #Box
        for i in range(0,9, 3):
            for j in range(0,9, 3):
                seen = set()
                for k in range(3):
                    for l in range(3):
                        if board[i+k][j+l] != '.':
                            if board[i+k][j+l] not in seen:
                                seen.add(board[i+k][j+l])
                            else:
                                return False
        return True
