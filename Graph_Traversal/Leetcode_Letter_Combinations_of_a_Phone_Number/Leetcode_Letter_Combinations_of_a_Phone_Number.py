##### My code #####
##### Runtime 59ms, Memory 14.4MB #####

def letterCombinations(self, digits: str) -> List[str]:   
    if not digits:
        return []

    res = []
    table = { '2' : 'abc', '3' : 'def', '4' : 'ghi', '5' : 'jkl',
              '6' : 'mno', '7' : 'pqrs', '8' : 'tuv', '9' : 'wxyz'}

    def dfs(index, path):
        if len(digits) <= index:
            res.append(path)
            return
        for i in table[digits[index]]:
            dfs(index + 1, path + i)
    dfs(0, '')
    return res