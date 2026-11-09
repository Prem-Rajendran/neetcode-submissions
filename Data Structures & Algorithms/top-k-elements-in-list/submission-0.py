class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = defaultdict(int)
        min_val = float('inf')
        max_val = float('-inf')
        for n in nums:
            hash_map[n] += 1

        reverse_map = defaultdict(list[int])
        for key in hash_map:
            min_val = min(min_val, hash_map[key])
            max_val = max(max_val, hash_map[key])
            reverse_map[hash_map[key]].append(key)

        result = []
        for i in range(max_val, min_val - 1, -1):
            if i in reverse_map:
                for x in reverse_map[i]:
                    result.append(x)
                    if len(result) == k:
                        return result

        return result
        

        