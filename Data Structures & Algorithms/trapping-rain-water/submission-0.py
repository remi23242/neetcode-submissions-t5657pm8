class Solution:
    def trap(self, height: List[int]) -> int:
        prefix=[]
        postfix=height.copy()
        postfix.pop(0)
        prefix.append(height[0])
        area=0

        for i,x in enumerate(height):
            if i>0 and i<len(height):
                value=min(max(prefix),max(postfix))-x
                if value>0:
                    area+=value
                prefix.append(x)
                postfix.pop(0)
        return area

        
            
            
                



        