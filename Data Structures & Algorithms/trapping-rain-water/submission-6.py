class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft=[]
        maxright=[]
        water=[]
        for x in height:
            if maxleft !=[]:
                if x > maxleft[-1]: 
                    maxleft.append(x)
                else:
                    maxleft.append(maxleft[-1])
            else:
                maxleft.append(x)
        for x in reversed(height):
            if maxright!=[]:
                if x> maxright[-1]:
                    maxright.append(x)
                else:
                    maxright.append(maxright[-1])
            else:
                maxright.append(x)
        maxright.reverse()
        minheight= [min(x,y) for x,y in zip(maxleft,maxright)]
        water=[x-y if x-y>0 else 0 for x,y in zip(minheight,height)]
        trappedwater= sum(water)
        return trappedwater


