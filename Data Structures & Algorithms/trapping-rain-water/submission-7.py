class Solution:
    def trap(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        trappedwater=0
        maxleft= height[0]
        maxright=height[j]
        while i<j:
            if maxleft < maxright: 
                i=i+1
                maxleft=max(maxleft, height[i])
                trappedwater += (maxleft-height[i])
            else:
                j=j-1
                maxright= max(maxright, height[j])
                trappedwater += (maxright-height[j])
        return trappedwater


            





       