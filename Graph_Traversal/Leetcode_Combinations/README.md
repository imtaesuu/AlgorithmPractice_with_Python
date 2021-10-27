## - Leetcode 77. Number of Islandss - [Link](https://leetcode.com/problems/combinations/)
● 입력  
> n = 4, k = 2

● 출력
> [  
  [2,4],  
  [3,4],  
  [2,3],  
  [1,2],  
  [1,3],  
  [1,4],  
]

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Graph_Traversal/Leetcode_Combinations/Leetcode_Combinations.py)

```python
def combine(n: int, k: int) -> List[List[int]]:
    temp, res = [], []

    def dfs(idx):
        if len(temp) == k:
            res.append(temp[:])
            return

        for i in range(idx, n + 1):
            temp.append(i)
            dfs(i + 1)
            temp.pop()

    dfs(1)
    return res
	
##### My code #####
##### Runtime 472ms, Memory 15.8MB #####
```

## - **How To Solve**
- **dfs**를 사용하여 깔끔히 풀이할 수 있는 조합 문제.
- n개 중 k개의 조합이니 temp의 길이가 k의 길이가 되면 결과값에 추가한다.
- n개는 1부터 n까지 나열한 숫자들이니 **range**를 사용하여 idx를 1씩 증가시키며 재귀한다.
- **itertools.combinations**를 사용하면 더욱 간편하고 빠르게 풀이할 수 있다.