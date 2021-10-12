##### My code #####
##### Runtime 316ms, Memory 16.9MB #####

def numIslands(grid: List[List[str]]) -> int:
    def dps(x, y):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != '1':
            return False

        grid[x][y] = '0'

        dps(x + 1, y)
        dps(x - 1, y)
        dps(x, y + 1)
        dps(x, y - 1)

    cnt = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dps(i,j)
                cnt += 1

    return cnt