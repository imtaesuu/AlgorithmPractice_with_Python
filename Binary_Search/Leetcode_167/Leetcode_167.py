##### Python 3 #####
##### Runtime 223ms, Memory 14.9MB #####

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, v in enumerate(numbers):
            t = target - v
            idx = bisect.bisect_left(numbers, t, i + 1)
            if idx < len(numbers) and numbers[idx] == t:
                return [i+1, idx + 1]