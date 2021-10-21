## - Leetcode 17. Letter Combinations of a Phone Number - [Link](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
● 입력  
> digits = "23"

● 출력
> ["ad","ae","af","bd","be","bf","cd","ce","cf"]

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Graph_Traversal/Leetcode_Letter_Combinations_of_a_Phone_Number/Leetcode_Letter_Combinations_of_a_Phone_Number.py)

```python
def letterCombinations(self, digits: str) -> List[str]:   
    if not digits:
        return []

    res = []
    table = { '2' : 'abc', '3' : 'def', '4' : 'ghi', '5' : 'jkl',
              '6' : 'mno', '7' : 'pqrs', '8' : 'tuv', '9' : 'wxyz'}

    def dfs(index, path):
        if len(digits) <= index:
            res.append(path)
            return
        for i in table[digits[index]]:
            dfs(index + 1, path + i)
    dfs(0, '')
    return res
	
##### My code #####
##### Runtime 59ms, Memory 14.4MB #####
```

## - **How To Solve**
- 생각보다 생각을 많이한 문제, 해당 테이블만 전체적으로 순환하면 되지만 for안에서 res에 append하면 안된다.
- 일종의 백트래킹 느낌으로 마지막까지 **dfs**로 도달했을 때 res에 append하는 식으로 코드를 작성헀다.
- 간단하다고 생각했고 실제로도 간단했지만 생각보다 시간을 많이 잡아먹은 문제였다.
- 많은 순환을 해야하는 문제일 때 백트래킹을 생각하자.