class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newlist= []
        for x in nums:
            if x in newlist:
                return True
            else:
                newlist.append(x)
        return False
            