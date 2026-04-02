from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s=Counter(list(s))
        count_t=Counter(list(t))
        if len(count_s)!=len(count_t):
            return False
        for x in count_s:
            if count_s[x]!=count_t[x]:
                return False
        return True