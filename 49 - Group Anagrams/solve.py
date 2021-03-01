class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_dict = {}
        for w in strs:
            cur_anagram_tuple = tuple(sorted(w))
            cur_anagram_map_hash = hash(cur_anagram_tuple)
            if cur_anagram_map_hash not in anagram_dict:
                anagram_dict[cur_anagram_map_hash] = [w]
            else:
                anagram_dict[cur_anagram_map_hash].append(w)
        return anagram_dict.values()
        