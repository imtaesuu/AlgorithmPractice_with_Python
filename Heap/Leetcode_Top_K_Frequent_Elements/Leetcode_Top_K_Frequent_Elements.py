##### My code #####
##### Runtime 145ms, Memory 18.9MB #####

def topKFrequent(nums: List[int], k: int) -> List[int]:        
    freqs = collections.Counter(nums)

    heap, res = [], []
    for val, freq in freqs.items():
        heapq.heappush(heap, (-freq, val))

    for _ in range(k):
        res.append(heapq.heappop(heap)[1])

    return res