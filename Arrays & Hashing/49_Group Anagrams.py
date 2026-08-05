# Methode 1: sort
# Methode 2: hash set

from collections import defaultdict

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         mp = defaultdict(list)
        
#         for str in strs:
#             arr = [0] * 26
#             for char in str:
#                 arr[ord(char)-ord('a')] += 1
#             mp[tuple(arr)].append(str)
#         return list(mp.values())

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)

        for str in strs:
            key = "".join(sorted(str))
            mp[key].append(str)

        return list(mp.values())