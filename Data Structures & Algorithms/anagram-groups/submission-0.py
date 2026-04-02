from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        length = defaultdict(list)
        for x in strs:
            count=[0]*26
            for y in x:
                count[ord(y)-ord('a')]+=1
            length[tuple(count)].append(x)
        return(list(length.values()))
