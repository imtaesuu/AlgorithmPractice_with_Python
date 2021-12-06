##### Python 3 #####
##### Runtime 80ms, Memory 14.6MB #####

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