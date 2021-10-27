##### My code #####
##### Runtime 472ms, Memory 15.8MB #####

def combine(n: int, k: int) -> List[List[int]]:
    temp, res = [], []

    def dfs(idx):
        if len(temp) == k:
            res.append(temp[:])
            return

        for i in range(idx, n + 1):
            temp.append(i)
            dfs(i + 1)
            temp.pop()

    dfs(1)
    return res