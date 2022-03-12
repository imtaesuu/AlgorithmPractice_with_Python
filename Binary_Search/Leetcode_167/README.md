## - Leetcode 167 Two Sum II - Input Array Is Sorted - [Link](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
● 입력  
>  numbers = [2,7,11,15], target = 9

● 출력
> [1,2]  

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Binary_Search/Leetcode_167/Leetcode_167.py)

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, v in enumerate(numbers):
            t = target - v
            idx = bisect.bisect_left(numbers, t, i + 1)
            if idx < len(numbers) and numbers[idx] == t:
                return [i+1, idx + 1]

##### Python 3 #####
##### Runtime 223ms, Memory 14.9MB #####
```

## - **How To Solve**
- bisect_left(a, x, lo=0, hi=len(a))를 이용하여 시작 길이 제한을 둠