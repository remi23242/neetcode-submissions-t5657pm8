class Solution:

    def encode(self, strs: List[str]) -> str:
        new=''
        for x in strs:
            new+=str(len(x))+"$"+ x
        return new


 


    def decode(self, s: str) -> List[str]:
        new=[]
        i=0
        while(i<len(s)):
            j=i
            while(s[j]!="$"):
                j+=1
            length=int(s[i:j])
            i=j+1
            j=i+length
            new.append(s[i:j])
            i=j
        return new

                


