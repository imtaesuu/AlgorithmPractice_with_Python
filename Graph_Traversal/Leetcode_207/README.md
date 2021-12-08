## - Leetcode 207. Course Schedule - [Link](https://leetcode.com/problems/course-schedule/)
● 입력   
> numCourses = 2, prerequisites = [[1,0],[0,1]]

● 출력
> false

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Graph_Traversal/Leetcode_207/Leetcode_207.py)

```python
def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = collections.defaultdict(list)
    for i, j in prerequisites:
        graph[i].append(j)

    def dfs(start):
        if start in visited:
            return False
        if start in vt:
            return True

        visited.add(start)
        for node in graph[start]:
            if not dfs(node):
                return False
        visited.remove(start)
        vt.add(start)

        return True

    visited = set()
    vt = set()

    for i in list(graph):
        if not dfs(i):
            return False
    return True
	
##### My code #####
##### Runtime 170ms, Memory 17.7MB #####
```

## - **How To Solve**
- 입력값을 딕셔너리 그래프로 만든 후 **dfs**로 순환하여 그래프가 순환하는 구조인지 파악하는 문제
- 문제를 제대로 이해해야 간단하게 풀 수 있다, 재귀함수로 구성하여 visited에 돌때마다 노드를 넣고
- 빠져올때마다 삭제하는 식으로 하여 예외적으로 무조건 false가 나오는 상황을 방지했다.
- 또 돌았던 노드를 만날 때 바로 true로 빠져나올 수 있도록 vt를 만들고 돌때마다 추가시켰다.