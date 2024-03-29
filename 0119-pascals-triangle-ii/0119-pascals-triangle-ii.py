class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        tria = [[] for _ in range(rowIndex + 1)]
        colNum = 1
        for r in range(rowIndex + 1):
            row = [1] * colNum
            tria[r] = row
            for c in range(1, colNum - 1):
                tria[r][c] = tria[r - 1][c - 1] + tria[r - 1][c]
            colNum += 1
        return tria[rowIndex]
        