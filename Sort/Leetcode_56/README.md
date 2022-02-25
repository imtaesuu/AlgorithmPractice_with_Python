## - Leetcode 56 Merge Intervals - [Link](https://leetcode.com/problems/merge-intervals/)
● 입력  
> intervals = [[1,3],[2,6],[8,10],[15,18]]

● 출력
>  [[1,6],[8,10],[15,18]]

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Sort/Leetcode_56/Leetcode_56.py)

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        # 입력값을 내부 리스트 앞의 값으로 정렬시킴
        for i in sorted(intervals, key = lambda x : x[0]):
            # res가 없을 때나 전 구간과 겹치는 부분이 없을 때는 res에 추가하고
            # 겹치는 부분이 있다면 전 구간의 마지막 값만 최대값으로 변경
            if res and i[0] <= res[-1][1]:
                res[-1][1] = max(i[1], res[-1][1])
            else:
                res.append(i)        
        return res
        
##### Python 3 #####
##### Runtime 198ms, Memory 18.1MB #####
```

## - **How To Solve**
- 포인트는 먼저 입력값을 정렬하는 것과, 전 구간의 마지막 값만 최대값으로 변경하면 된다는 점
- 굳이 두 구간을 합해서 최대값을 구하지 않고 두 구간의 오른쪽 값들로만 비교
- 필요한 부분만 변경하는 깔끔한 풀이는 어렵지만 어떻게든 구현은 가능한 문제
