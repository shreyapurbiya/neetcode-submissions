class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        substring=[]
        substring2=[]
        maxlength=0
        for x in s:
            if x not in substring:
                substring.append(x)
                if maxlength<len(substring):
                    maxlength = len(substring)
            else:
                substring=substring[substring.index(x) + 1:]
                substring.append(x)
        return maxlength

        
        
        
        
        if len(substring2)>len(substring):
            return len(substring2)
        else: 
            return len(substring)

        

