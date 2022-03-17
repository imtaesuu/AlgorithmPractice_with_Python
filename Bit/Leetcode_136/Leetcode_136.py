##### Python 3 #####
##### Runtime 191ms, Memory 16.7MB #####

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            # ^ 는 XOR 연산
            # 같은 값이 나오면 0으로 초기화됨을 이용    
            # 나왔던 값이 나오면 0이 초기화되고 한번만 나오면 그 값으로 유지
            result ^= num
        return result