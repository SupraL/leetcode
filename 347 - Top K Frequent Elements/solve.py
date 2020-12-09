class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        r_map = {}
        for n in nums:
            r_map[n] = 1 if n not in r_map else r_map[n] + 1
        return sorted(r_map, key=r_map.get)[::-1][:k]