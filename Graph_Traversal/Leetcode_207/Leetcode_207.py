##### My code #####
##### Runtime 170ms, Memory 17.7MB #####

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