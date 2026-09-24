class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countN = {}
        for i in range(len(nums)):
            countN[nums[i]] = 1 + countN.get(nums[i],0)
        heap = []
        for num, count in countN.items():
            heapq.heappush(heap,(count,num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for count, num in heap]