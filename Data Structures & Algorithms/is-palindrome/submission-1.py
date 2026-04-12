class Solution:
    def isPalindrome(self, s: str) -> bool:
        s="".join(s.split())
        s="".join(char for char in s if char.isalnum())
        s=s.lower()
        left=0
        for right in range(len(s)-1,-1,-1):
            if right==left:
                return True
            if s[right]!=s[left]:
                return False
            left+=1
        return True
        
        