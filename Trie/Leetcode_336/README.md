## - Leetcode 336 Palindrome Pairs - [Link](https://leetcode.com/problems/palindrome-pairs/)
● 입력  
> words = ["abcd","dcba","lls","s","sssll"]

● 출력
> [[0,1],[1,0],[3,2],[2,4]]

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Tree/Leetcode_336/Leetcode_336.py)

```python
class TrieNode:
    def __init__(self):
        #  기본적인 Trie에 입력값 리스트의 index, 와 palindrome 여부를 확인하는 리스트를 추가
        self.idx = -1
        self.children = collections.defaultdict(TrieNode)
        self.palindrome_list = []

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def is_palindrome(self, word: str) -> bool:
        return word == word[::-1]
    
    def insert(self, idx: int, word: str) -> None:
        node = self.root
        # 제일 중요한건 Trie를 만들 때 팰린드롬을 확인하는 것이기에 값을 거꾸로 넣어줄 것
        # 또한 넣으면서 동시에 넣기 전의 word가 팰린드롬일 경우 팰린드롬 리스트에 넣어주어 탐색시 시간 최소화
        # 마지막 값에 단어의 끝을 알리는 index값을 넣어줄 것
        for i, v in enumerate(word[::-1]):
            if self.is_palindrome(word[:len(word)-i]):
                node.palindrome_list.append(idx)
            node = node.children[v]
        node.idx = idx
        
    def search(self, idx: int, word: str) -> List[List[int]]:
        node = self.root
        res = []
        
        # 탐색 도중 다른 word의 끝값과 만났다면 남은 값들이 팰린드롬인지 판별하고 res에 추가
        # 남은 값들이 팰린드롬이다면 어차피 탐색 도중 만난 word와 입력받은 word가 같은 단어를 포함하고 있으면서
        # 역순 배치이기 때문에 팰린드롬임
        for i, v in enumerate(word):
            if node.idx >= 0:
                if self.is_palindrome(word[i:]):
                    res.append([idx, node.idx])

            if v not in node.children:
                return res

            node = node.children[v]
         
        # 끝까지 탐색 후 단어의 끝을 발견했다면 추가, 주의할 점은 같은 단어끼리 묶으면 안되기에 예외를 설정해줄 것
        if node.idx >= 0 and node.idx != idx:
            res.append([idx, node.idx])
        
        # 끝까지 탐색 후 팰린드롬 리스트에 있는 idx들도 다 더해줌
        for p in node.palindrome_list:
            res.append([idx, p])        
                
        return res
    
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()
        res = []
        
        for i, v in enumerate(words):
            trie.insert(i, v)
        
        for i, v in enumerate(words):
            res += trie.search(i, v)
        
        return res

##### Python 3 #####
##### Runtime 4768ms, Memory 400.4MB #####
```

## - **How To Solve**
- Trie 자료구를 이용하여 시간초과를 피해야하는 문제
- 판별을 여러번 거쳐야 하고, Trie를 거꾸로 만들어야 하는 게 포인트
