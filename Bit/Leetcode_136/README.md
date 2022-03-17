## - Leetcode 136 Single Number - [Link](https://leetcode.com/problems/single-number/)
● 입력  
>  nums = [4,1,2,1,2]

● 출력
> 4

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Bit/Leetcode_136/Leetcode_136.py)

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            # ^ 는 XOR 연산
            # 같은 값이 나오면 0으로 초기화됨을 이용    
            # 나왔던 값이 나오면 0이 초기화되고 한번만 나오면 그 값으로 유지
            result ^= num
        return result

##### Python 3 #####
##### Runtime 191ms, Memory 16.7MB #####
```

## - **How To Solve**
- XOR 비트 연산을 통해 문제를 해결함
- collections.Counter의 most_common을 이용하여도 풀이가능