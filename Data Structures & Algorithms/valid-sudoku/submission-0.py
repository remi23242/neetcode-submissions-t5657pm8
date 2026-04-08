class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for y in range(len(board)):
            check_col=set()
            check_row=set()
            for x in range(len(board[y])):
                if board[x][y]!='.':
                    if board[x][y] in check_row:
                        return False
                    else: 
                        check_row.add(board[x][y])
                if board[y][x]!='.':
                    if board[y][x] in check_col:
                        return False
                    else:
                        check_col.add(board[y][x])
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
 

                
        return True