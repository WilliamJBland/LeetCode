class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        squares = [[] for _ in range(len(board))]
        columns = [[] for _ in range(len(board))]
        j, i = 0, 0
        for row in board:
            squares[j].extend(row[:3])
            squares[j+1].extend(row[3:6])
            squares[j+2].extend(row[6:9])
            i += 1
            if i % 3 == 0:
                j += 3
            if len(set(row) - {"."}) != len([r for r in row if r != "."]):
                return False
            for ind, c in enumerate(row):
                columns[ind].append(c)

        for i in range(len(columns)):
            c, s = columns[i], squares[i]
            if len(set(c) - {"."}) != len([r for r in c if r != "."]) or len(set(s) - {"."}) != len([r for r in s if r != "."]):
                return False
        return True