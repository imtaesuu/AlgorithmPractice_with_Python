##### Python 3 #####
##### Runtime 176ms, Memory 32.1MB #####

# 트라이를 위한 노드 클래스
class TrieNode:
    def __init__(self):
        self.word = False
        self.next = collections.defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        # defaultdict를 이용했기 때문에 node.next[w]를 작성한 순간부터 w를 key값으로 가지는 해쉬 생성
        for w in word:
            node = node.next[w]
        # 단어의 끝은 True로 표시
        node.word = True

    def search(self, word: str) -> bool:
        node = self.root
        for w in word:
            # 시간 단축과 메모리 절감을 위해 dict에 없을 경우 바로 False 리턴
            if w not in node.next:
                return False
            node = node.next[w]
        
        # 단어의 끝인지를 확인하기 위함이니 True가 아닌 node.word값을 리턴
        return node.word
            

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        
        for p in prefix:
            if p not in node.next:
                return False
            node = node.next[p]
    
        # search 기능과는 다르게 포함만 해도 True
        return True
        