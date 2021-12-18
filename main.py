import sys, datetime , math, itertools
from collections import Counter, defaultdict
import heapq
    
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
    


<<<<<<< HEAD
N, L, F = input().split()
=======
        print(p)
    elif cmd == 'add':
        p, l, g = map(int, args)
        add_pb(p, l, g)
    else:
        problem_dict[int(args[0])] = 0
    test 
        
        
        
        
        
        
        
        
        
>>>>>>> 360834c5f5b55cf27b8c68104ed33f5d5d43cc73

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
else:
    print(-1)
            
            
        

        