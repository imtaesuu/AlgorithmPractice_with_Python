## - Leetcode 179 Largest Numbert - [Link](https://leetcode.com/problems/largest-number/)
● 입력  
> nums = [3,30,34,5,9]

● 출력
>  "9534330"

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Sort/Leetcode_179/Leetcode_179.py)

```python
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 처음부터 원래 자리로 순회 다시 돌아오는 것을 방지하기 위해 포인터를 저장해둠 
        pointer = 1
        while pointer < len(nums):
            # 앞으로 이동하며 스왑을 해야되기 때문에 현재 위치를 따로 저장
            # 앞의 위치를 -1을 함으로 표현 했으니 cur은 항상 0보다 커야함
            # 스왑한 후가 스왑하기 전보다 크다면 스왑해줌
            cur = pointer
            while cur > 0 and self.is_swap(nums[cur-1], nums[cur]):
                nums[cur-1], nums[cur] = nums[cur], nums[cur-1]
                cur -= 1
            # 정렬이 끝나면 포인터는 한칸씩 전진해줌
            pointer += 1
        
        # [0, 0] 등 입력값이 0으로만 이루어져 있을 때 '00'으로 나오는 것을 방지하기 위해
        # str(int(...)) 작업을 해주어 '0'으로 만들어줌
        return str(int(''.join(map(str, nums))))
        
    def is_swap(self, nums1, nums2):
        return str(nums1) + str(nums2) < str(nums2) + str(nums1)

### Python 3 #####
##### Runtime 115ms, Memory 13.9MB #####
```

## - **How To Solve**
- 두개의 문자형 숫자를 합치면서 스왑 전과 후 중 무엇이 더 큰 지 판단해야함
- 시간초과를 최대한 방지하기 위해 고정된 위치값과 스왑시 필요한 위치값을 따로 만듦
