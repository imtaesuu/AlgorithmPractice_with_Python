## - Leetcode 33 Search in Rotated Sorted Array - [Link](https://leetcode.com/problems/search-in-rotated-sorted-array/)
● 입력  
> nums = [4,5,6,7,0,1,2], target = 0

● 출력
>  4

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Binary_Search/Leetcode_33/Leetcode_33.py)

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 입력값 예외 처리
        if not nums:
            return -1
        
        # 먼저 정렬된 배열에서의 가장 작은값의 idx를 찾아야 됨
        # 이유는 어떤 수가 pivot으로 선정되어 회전되었는지 알 수 없기 때문임
        # 가장 작은값이 얼마나 회전 되었는지 확인하면됨
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right - left)//2
            
            # left가 가장 작은수의 위치를 알려주는 구조
            # mid값이 right값보다 크다면 left가 mid값 한칸뒤로 땡겨짐
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        pivot = left
        
        # 얼마나 회전되었는지 알았으니 이제부터는 target을 찾으면 됨
        # 일반적인 이진검색에서 회전값 즉 pivot에 더해주어 찾으면 됨
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left)//2
            
            # mid + pivot이 길이를 초과하지 않게 나머지값을 활용
            mid_pivot = (mid + pivot) % len(nums)
            
            if nums[mid_pivot] < target:
                left = mid + 1
            elif nums[mid_pivot] > target:
                right = mid - 1
            else:
                return mid_pivot
        return -1
        
##### Python 3 #####
##### Runtime 40ms, Memory 14.2MB #####

```

## - **How To Solve**
- 단순 list의 index 기능을 써도 되지만 문제의 의도에 맞게 이진검색만을 활용하여 풀이함
- 리스트가 길이를 초과하지 않고 제한된 범위에서 회전하기 때문에 mid + pivot의 나머지값을 활용
- mid_pivot의 값을 target과 비교하여 left, right에 mid +- 1 값을 넣어줌
