## - Leetcode 200. Number of Islandss - [Link](https://leetcode.com/problems/number-of-islands/)
● 입력  
> grid = [  
  ["1","1","1","1","0"],  
  ["1","1","0","1","0"],  
  ["1","1","0","0","0"],  
  ["0","0","0","0","0"]  
]

● 출력
> 1
## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Graph_Traversal/Leetcode_Number_of_Islands/Leetcode_Number_of_Islands.py)

```python
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
	
##### My code #####
##### Runtime 316ms, Memory 16.9MB #####
```

## - **How To Solve**
- 전형적인 **dps** 문제이다.
- 재귀구조로 풀이하였고, 타임아웃에 막힌다면 **스택**을 이용하여 탐색해도된다.