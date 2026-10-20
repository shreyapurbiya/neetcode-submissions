class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charlist1= list(s)
        charlist1.sort()
        charlist2 = list(t)
        charlist2.sort()
        if charlist1 == charlist2:
            return True
        return False
        

