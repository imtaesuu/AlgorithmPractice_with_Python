## - Leetcode 332. Reconstruct Itinerary - [Link](https://leetcode.com/problems/reconstruct-itinerary/)
● 입력  
> tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]  

● 출력
> ["JFK","ATL","JFK","SFO","ATL","SFO"]  

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Graph_Traversal/Leetcode_Reconstruct_Itinerary/Leetcode_Reconstruct_Itinerary.py)

```python
def findItinerary(tickets: List[List[str]]) -> List[str]:
    table = collections.defaultdict(list)
    res = []

    for t in sorted(tickets, reverse = True):
        table[t[0]].append(t[1])

    def dfs(node):
        while table[node]:
            dfs(table[node].pop())
        res.append(node)

    dfs('JFK')
    return res[::-1]
	
##### Python 3 #####
##### Runtime 80ms, Memory 14.6MB #####
```

## - **How To Solve**
- 예제만 생각하면 그냥 단순히 정렬해서 dfs로 뽑아내면 되는 문제
- 하지만 어휘순으로 더 빠른 곳임에도 길이 끊기는 경우가 있기 때문에 처리를 따로 해줘야함
- res에 재귀가 끝날 때마다 node를 더해준 후 마지막 결과값은 거꾸로 뒤집어 주면 됨.
- 단순하지만 예외상황 때문에 까다로운 문제, 항상 예외상황을 생각하면서 풀이할 것