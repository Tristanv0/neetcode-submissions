class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        grid = {}
        row_set = [set() for i in range(9)]
        col_set = [set() for i in range(9)]
        for i in range(3):
            for j in range(3):
                grid[(i,j)] = set()

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != '.':
                    # check if valid 3x3
                    if board[i][j] in grid[(i//3,j//3)]:
                        return False
                    else:
                        grid[(i//3,j//3)].add(board[i][j])
                    
                    # check if valid row
                    if board[i][j] in row_set[i]:
                        return False
                    else:
                        row_set[i].add(board[i][j])
                    
                    # check if valid col
                    if board[i][j] in col_set[j]:
                        return False
                    else:
                        col_set[j].add(board[i][j])

        return True
                    
                