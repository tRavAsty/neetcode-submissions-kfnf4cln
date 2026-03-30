class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        found = False
        for i in range(m):
            for j in range(n):
                if not found and board[i][j] == word[0]:
                    queue = [(i, j, 0,set())]
                    while queue:
                        row, col, index, visited = queue.pop(0)
                        if index == len(word):
                            found = True
                            break

                        if row < 0 or row >= m or col < 0 or col >= n or (row,col) in visited or board[row][col] != word[
                            index]:
                            continue

                        visited.add((row,col))
                        new_index = index + 1
                        queue.append((row - 1, col, new_index, visited.copy()))
                        queue.append((row, col - 1, new_index,visited.copy()))
                        queue.append((row + 1, col, new_index,visited.copy()))
                        queue.append((row, col + 1, new_index,visited.copy()))
        return found
        