class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count =0
        difflist=[]
        i=0
        while i<(len(nums)-1):
            prev=nums[i]
            i=i+1
            diff=nums[i]-prev
            if diff == 1:
                count=count+1
                difflist.append(count)
            elif prev==nums[i]:
                continue
            else:
                difflist.append(count)
                count=0
        if nums != [] and len(nums)!=1 and len(set(nums))!=1:
            count = max(difflist)
            count =count+1
        elif len(nums)==1 or len(set(nums))==1:
            count=1
        return(count)
