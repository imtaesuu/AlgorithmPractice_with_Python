## - Leetcode 39. Combination Sum - [Link](https://leetcode.com/problems/combination-sum/)
● 입력  
> candidates = [2,3,5], target = 8

● 출력
> [[2,2,2,2],[2,3,3],[3,5]]

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Graph_Traversal/Leetcode_Combination_Sum/Leetcode_Combination_Sum.py)

```python
def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    res, temp = [], []

    def dfs(idx, num):
        if num >= target:
            if num == target:
                res.append(temp[:])
            return

        for i in range(idx, len(candidates)):
            temp.append(candidates[i])
            num += candidates[i]
            dfs(i, num)
            temp.pop()
            num -= candidates[i]

    dfs(0, 0)
    return res
	
##### My code #####
##### Runtime 84ms, Memory 14.3MB #####
```

## - **How To Solve**
- **dfs**를 사용하여 조합의 합과 자리를 계속 넘기며 재귀풀이 한 문제
- 조합의 합이 target보다 같으면 결과값에 추가하고 리턴하도록 구현
- 기존 조합 문제에서 num을 이용하여 조합의 합을 이용