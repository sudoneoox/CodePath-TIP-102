from typing import List


def local_maximums(grid: List[List[int]]) -> List[List]:
    """
    return local maximum in every continuous 3x3 matrix in grid
    """
    if not grid or len(grid) < 3 or len(grid[0]) < 3:
        return []

    rows: int = len(grid)
    cols: int = len(grid[0])
    result: List[List[int]] = []

    for i in range(rows - 2):
        row_result = []
        for j in range(cols - 2):
            local_max = -9999999

            # iterate 3x3 matrix
            for di in range(3):
                for dj in range(3):
                    local_max = max(local_max, grid[i + di][j + dj])
            row_result.append(local_max)
        if row_result:
            result.append(row_result)

    return result


grid = [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]
print(local_maximums(grid))
