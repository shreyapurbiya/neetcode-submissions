class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        substring=set()
        maxlength=0
        left=0
        right=0
        while right< len(s):
            if s[right] not in substring:
                substring.add(s[right])
                if maxlength<len(substring):
                    maxlength = len(substring)
                right+=1
            else:
                while s[right] in substring:
                    substring.remove(s[left])
                    left += 1
        return maxlength

        
        
        
        
        if len(substring2)>len(substring):
            return len(substring2)
        else: 
            return len(substring)