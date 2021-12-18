## - Baekjoon 21942 부품 대여장 - [Link](https://www.acmicpc.net/problem/21942)
● 입력  
> 8 014/00:00 5  
2021-01-01 09:12 arduino tony9402  
2021-01-13 13:24 arduino tony9402  
2021-01-23 14:04 raspberrypi tony9402  
2021-02-01 18:21 resistance amsminn  
2021-02-03 23:14 transistor codethinking  
2021-02-08 22:14 transistor codethinking  
2021-02-09 12:45 resistance amsminn  
2021-02-13 14:37 raspberrypi tony9402     

● 출력
> tony9402 50565 

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Data_Structure/Baekjoon_21942/Baekjoon_21942.py)

```python
import sys, datetime, math
from collections import defaultdict
input = sys.stdin.readline

# 문자열을 datetime으로 바꿔주는 함수
def get_datetime(day, time):
    Y, M, D = map(int, day.split('-'))
    h, m = map(int, time.split(':'))
    return datetime.datetime(Y, M, D, h, m)

# 해당 user가 item을 빌렸는지 체크하는 함수
def check_item(user, item):
    for key in table[user].keys():
        if key == item and table[user][item] != 0:
            return True
    return False
    
N, L, F = input().split()

# 미리 대여 기간을 datetime으로 전환
period = datetime.timedelta(days=int(L[:3]), hours=int(L[4:6]), minutes=int(L[7:]))
table, res = defaultdict(dict), defaultdict(int)

for _ in range(int(N)):
    args = input().split()
    
    if not check_item(args[3], args[2]):
        # user : { item : (day, time) } 의 형식으로 table 구성
        table[args[3]][args[2]] = (args[0], args[1])
        continue
    
    # user가 해당 item을 대여하고 있을 때 반납일자와 대여당일 일자의 차이를 datetime으로 변환
    # 차이값과 기간값을 초로 바꾸고 차이값 - 기간값을 한 후 60을 나누어 분으로 바꾸어줌
    diff = get_datetime(args[0], args[1]) - get_datetime(table[args[3]][args[2]][0], table[args[3]][args[2]][1])
    minutes = (diff.total_seconds() - period.total_seconds())/60
    
    # 대여기간 초과시 초과분당 벌금을 곱해주고 0.0001초라도 초과되면 벌금이기에 올림해줌 
    if minutes > 0:
        res[args[3]] += math.ceil(minutes*int(F))
    table[args[3]][args[2]] = 0

# 결과값을 순차적으로 출력, 없을시 -1 출력
if res:
    for user in sorted(res.keys()):
        print(user, res[user])
else: print(-1)
	
##### Python 3 #####
##### Runtime 564ms, Memory 59980KB #####
```

## - **How To Solve**
- dict와 내장함수 datetime을 이용하여 풀이한 문제
- 주의할점은 부품이 한개가 아니고 여러개 있다는 전제하에서 문제를 풀이해야하는 것
- list를 이용하는 방법도 있겠지만, 본인은 dict안에 dict를 넣어서 좀더 간결하게 풀이함
- 구현도 크게 어렵지 않고 주어진 user와 item의 수가 적어 시간초과 걱정도 크게 없었던 문제