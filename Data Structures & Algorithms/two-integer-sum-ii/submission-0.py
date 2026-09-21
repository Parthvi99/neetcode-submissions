class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(numbers):
            diff = target - n 
            if diff in seen:
                a = seen[diff] + 1
                b = i + 1
                return [a,b]
            seen[n] = i
        return []
        