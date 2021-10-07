## - Leetcode 3. Longest Substring Without Repeating Characters - [Link](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
● 입력  
> "pwwkew"

● 출력
> 3

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Stack_and_Queue/Baekjoon_1874/Baekjoon_1874.py)

```python
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
	
##### My code #####
##### Runtime 88ms, Memory 14.2MB #####
```

## - **How To Solve**
- 위치 포인터 두개를 사용하여 두개를 각각 증가시키면서 중복문자를 확인한다.
- 포인터가 증가할때 마다 결과값에 **max**를 이용하여 항상 결과값이 최대값이 되도록한다.
- 내 코드는 좀 더 두개의 포인터에 집중했다면 책에서는 **해시 테이블**을 이용하였다.
- 책의 코드가 좀더 가독성있고 다른 문제에서도 이용하기 쉬운 코드인 것 같다.
- 좀더 유연한 사고방식을 가지면 무작정 구현에 매달리지 않고 이 문제를 풀 수 있을듯 하다.
