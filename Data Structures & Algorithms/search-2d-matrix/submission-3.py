class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        # Find target row 

        # Check middle row first element
        row_min = 0
        row_max = m - 1
        target_row = -1
        while (row_min <= row_max) :
            mid_row = (row_min + row_max) // 2
            if target < matrix[mid_row][0] :
                row_max = mid_row - 1
            elif target > matrix[mid_row][0] :
                if mid_row + 1 < m and target < matrix[mid_row + 1][0] :
                    target_row = mid_row
                    break
                elif mid_row + 1 >= m:
                    target_row = mid_row
                    break
                else : 
                    row_min = mid_row + 1
            else:
                target_row = mid_row
                break


        # Check for target in target row
        col_min = 0
        col_max = n - 1
        while (col_min <= col_max) :
            mid_col = (col_min + col_max) // 2
            if target < matrix[target_row][mid_col] : 
                col_max = mid_col - 1
            elif target > matrix[target_row][mid_col] :
                col_min = mid_col + 1
            else: 
                return True

        return False
