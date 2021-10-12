## - Leetcode 347. Top K Frequent Elements - [Link](https://leetcode.com/problems/top-k-frequent-elements/)
● 입력  
> nums = [1,1,1,2,2,3], k = 2

● 출력
> [1,2]
## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Heap/Leetcode_Top_K_Frequent_Elements/Leetcode_Top_K_Frequent_Elements.py)

```python
def topKFrequent(nums: List[int], k: int) -> List[int]:        
    freqs = collections.Counter(nums)

    heap, res = [], []
    for val, freq in freqs.items():
        heapq.heappush(heap, (-freq, val))

    for _ in range(k):
        res.append(heapq.heappop(heap)[1])

    return res
	
##### My code #####
##### Runtime 145ms, Memory 18.9MB #####
```

## - **How To Solve**
- 우선순위 큐를 이용해도 되지만 보편적으로 파이썬에서는 **heapq**를 많이 사용한다.  
- 입력된 리스트를 받아 **Counter**를 이용하여 딕셔너리 상태로 만들었다.  
- **heapq**는 최소힙으로 구현되어 있기때문에 큰 것부터 꺼내려면 빈도수를 음수로 만들어준다.
- **heapq**를 알고 있으면 손쉽게 풀 수 있는 문제이다.
