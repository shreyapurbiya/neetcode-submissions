class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newlist= []
        for x in nums:
            if x not in newlist:
                newlist.append(x)
            else:
                return True
        return False
            