##### Python 3 #####
##### Runtime 198ms, Memory 18.1MB #####

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        # 입력값을 내부 리스트 앞의 값으로 정렬시킴
        for i in sorted(intervals, key = lambda x : x[0]):
            # res가 없을 때나 전 구간과 겹치는 부분이 없을 때는 res에 추가하고
            # 겹치는 부분이 있다면 전 구간의 마지막 값만 최대값으로 변경
            if res and i[0] <= res[-1][1]:
                res[-1][1] = max(i[1], res[-1][1])
            else:
                res.append(i)        
        return res