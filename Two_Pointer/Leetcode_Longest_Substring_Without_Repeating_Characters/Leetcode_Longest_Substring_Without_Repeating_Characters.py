##### My code #####
##### Runtime 88ms, Memory 14.2MB #####

def lengthOfLongestSubstring(s: str) -> int:
    if not s:
        return 0

    p1, p2, res = 0, 0, 1

    while p1 + 1 < len(s) and p2 + 1 < len(s):
        temp = s[p1:p2+1]

        if s[p2+1] in temp:
            p1 += 1
            continue
        else:
            p2 += 1
            res = max(res, p2 - p1 + 1)

    return res