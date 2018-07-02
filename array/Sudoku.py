class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            hang = board[i]
            lie = []
            for j in range(9):
                lie.append(board[j][i])
            for m in hang:
                if hang.count(m)>1 and m!='.':
                    return False
            for n in lie:
                if lie.count(n)>1 and n!='.':
                    return False
            for j in range(1, 10):
                if i%3==0 and j%3==0:
                    small = []
                    for p in range(i,i+3):
                        for q in range(j,j+3):
                            if board[p][q] != '.':
                                small.append(board[p][q])
                    if len(small) != len(list(set(small))):
                        # print i,j,p,q
                        return False
        return True

    def isValidSudoku1(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        sl = lambda row1, row2, col1, col2, lst: \
            [lst[r][col1:col2] for r in range(row1, row2)]
        subBoard = []
        for i in range(9):
            row = board[i]
            column = [x[i] for x in board]
            subBoard = sl(int(i/3)*3, int(i/3)*3+3, i%3*3, i%3*3+3, board)
            subBoard = [n for a in subBoard for n in a]
            b = [a for a in subBoard]

            for j in range(9):
                if row.count(str(j)) > 1:
                    return False
                if column.count(str(j)) > 1:
                    return False
                if subBoard.count(str(j)) > 1:
                    return False
        return True





if __name__ == "__main__":
    a = [["5","3",".",".","7",".",".",".","."],
          ["6",".",".","1","9","5",".",".","."],
          [".","3","8",".",".",".",".","6","."],
          ["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],
          [".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]]
    b = [
          ["8","3",".",".","7",".",".",".","."],
          ["6",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],
          ["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],
          [".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]
        ]
    c = [
            [".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".","."],
            [".","9",".",".",".",".",".",".","1"],
            ["8",".",".",".",".",".",".",".","."],
            [".","9","9","3","5","7",".",".","."],
            [".",".",".",".",".",".",".","4","."],
            [".",".",".","8",".",".",".",".","."],
            [".","1",".",".",".",".","4",".","9"],
            [".",".",".","5",".","4",".",".","."]
         ]
    s = Solution()
    print(s.isValidSudoku1(c))