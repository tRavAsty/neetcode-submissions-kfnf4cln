class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValidArray(nums:List):
            seen = set()
            for e in nums:
                if e!="." and e in seen:
                    return False
                else:
                    seen.add(e)
            return True

        def isValidRow(i:int):
            nums = board[i]
            return isValidArray(nums)

        def isValidCol(i:int):
            nums = [board[j][i] for j in range(n)]
            return isValidArray(nums)
        
        def isValidSub(i:int):
            row = (i//3)*3
            col = (i%3)*3
            nums = []
            for j in range(3):
                for k in range(3):
                    nums.append(board[row+j][col+k])
            print(f"Sub {i}")
            return isValidArray(nums)

        n = 9
        for i in range(9):
            if not isValidRow(i) or not isValidCol(i) or not isValidSub(i):
                return False
        return True


    



        