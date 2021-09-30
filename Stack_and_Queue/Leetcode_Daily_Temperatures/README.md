## - Leetcode 739. Daily Temperatures - [Link](https://leetcode.com/problems/daily-temperatures/)
● 입력  
> [73,74,75,71,69,72,76,73] 

● 출력
> [1,1,4,2,1,1,0,0]

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Stack_and_Queue/Leetcode_Daily_Temperatures/Leetcode_Daily_Temperatures.py)

```python
def dailyTemperatures(temperatures):
    rlt = [0]*len(temperatures)
    dic = {}
    Stack = []

    for idx, val in enumerate(temperatures):
        dic[idx] = val

    for idx, temp in dic.items():
        while Stack and dic.get(Stack[-1]) < temp:
            rlt[Stack[-1]] = idx - Stack[-1]
            Stack.pop()
        Stack.append(idx)

    return rlt
	
##### My code #####
##### Runtime 1340ms, Memory 35MB #####
```

## - **How To Solve**
- 입력값의 길이에 따라 **초기값을 0**으로 하는 결과값 리스트를 먼저 만든다.
- 현재의 **인덱스**를 계속 쌓아두다가 더 큰 값을 만났을 때 결과값에 차이가 반영되게끔 **스택**을 이용했다.
-  **enumerate**를 이용하여 입력값에 **인덱스**를 붙이고, **딕셔너리 값**을 순회할 때 **인덱스**를 **스택**에 쌓는다.
- 쌓인 **스택**의 **후입온도**와 **현재온도**를 비교하여 현재의 온도가 더 크다면 **인덱스** 차이만큼을 결과값에 입력한다.
- **0을 초기값**으로 하여 자신보다 큰값을 못만난 값들은 0으로 유지된다.