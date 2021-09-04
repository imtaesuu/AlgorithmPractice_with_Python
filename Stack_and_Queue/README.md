# Stack and Queue

## - Leetcode 20. Valid Parentheses - [Link](https://leetcode.com/problems/valid-parentheses/)
● 입력  
> ([{}])()[]{} 

● 출력
> __True__  

## - 책을 보며 이해한 풀이 - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Stack_and_Queue/Leetcode_Valid_Parentheses.py) 
괄호가 __유효__ 하게 입력 되었는지, 같은 괄호끼리 __대칭적__ 으로 입력 되었는지 확인하는 문제이다.   
깔끔하고 명료한 코드를 작성하지 못하여 책을 보며 __Stack__ 을 이용한 풀이방법에 대한 힌트를 얻었다.
```python
stack = []
table = {
	')' : '(',
	']' : '[',
	'}' : '{'
}
```
먼저 __Stack__ 으로 이용할 리스트를 생성하고, 괄호의 정보가 담긴 __table__ 을 생성한다.  
__table__ 에는 닫는 괄호를 __key__ 로, 여는 괄호를 __value__ 로 사용하여  
__Stack__ 에 __value__ 값을 __push__ 하여 가장 안에 있는 괄호를 가장 먼저 __pop__ 하여 확인할 수 있도록 한다.

```python
for char in s:
	if char not in table:
		stack.append(char)
	elif not stack or table[char] != stack.pop():
		return False
return len(stack) == 0
```
하나씩 입력값을 받으며, 닫는 괄호가 아니면 __push__ 하도록 하고,  
닫는 괄호인데 __Stack__ 에 아무것도 없거나  
혹은 가장 안쪽에 있는 괄호를 꺼내여 __table__ 에서 해당하는 __value__ 값이 일치하지 않을 때 __False__ 을 반환한다.    	
최종적으로 __Stack__ 의 길이가 0일 때와 아닐때의 __bool__ 값을 받아 반환한다. 아래는 최종 코드이다.
```python
def isValid(self, s: str) -> bool:
    stack = []
    table = {
        ')' : '(',
        ']' : '[',
        '}' : '{'
    }

    for char in s:
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False
    return len(stack) == 0
	
##### The answer in the book #####
##### Runtime 50ms, Memory 14.1MB #####
```
