class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = dict()

        if len(nums) <= 2:
            return [0, 1]

        for i, n in enumerate(nums):

            if n in hash_map:
                return [hash_map[n], i]

            result = target - n
            hash_map[result] = i

        return []
