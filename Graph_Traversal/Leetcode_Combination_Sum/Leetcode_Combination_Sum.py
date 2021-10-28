##### My code #####
##### Runtime 84ms, Memory 14.3MB #####

def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    res, temp = [], []

    def dfs(idx, num):
        if num >= target:
            if num == target:
                res.append(temp[:])
            return

        for i in range(idx, len(candidates)):
            temp.append(candidates[i])
            num += candidates[i]
            dfs(i, num)
            temp.pop()
            num -= candidates[i]

    dfs(0, 0)
    return res