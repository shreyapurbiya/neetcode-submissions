class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        j = 0
        for row in board:
            values = [x for x in row if x != "."]
            if len(values) != len(set(values)):
                return False
            
        while j < len(board[0]):
            i = 0  # reset to the first row
            col = []
            box=[]
            while i < len(board):
                if board[i][j] != ".":
                    col.append(board[i][j])
                i += 1
            if len(col) != len(set(col)):  #checking duplicates in a column
                return False
            j+=1
        
        i=0
        j=0
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                box = []
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        if board[i][j] != ".":
                            box.append(board[i][j])
                        j=j+1
                    i=i+1
                if len(box) != len(set(box)):  #checking duplicates in a square
                    return False
        return True
        




    
