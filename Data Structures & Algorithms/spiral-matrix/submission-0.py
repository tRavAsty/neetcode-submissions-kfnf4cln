class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        last_r,last_c = 0,0
        res = [matrix[last_r][last_c]]
        index = 0
        visited = set([(0,0)])
        while len(res)!=n*m:
            tmp_r,tmp_c = last_r+dirs[index][0],last_c+dirs[index][1]
            if tmp_r>=n or tmp_r<0 or tmp_c>=m or tmp_c<0 or (tmp_r,tmp_c) in visited:
                index = (index+1)%4
                continue
            res.append(matrix[tmp_r][tmp_c])
            visited.add((tmp_r,tmp_c))
            last_r,last_c = tmp_r,tmp_c
        return res
            






        