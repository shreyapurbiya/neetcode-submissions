class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums= sorted(nums)
        i=0
        triplets=[]
        while i<len(nums):
            j=i+1
            k=len(nums)-1
            if i == 0 or nums[i] != nums[i-1]:
                while j<k:
                        if nums[i]+nums[j]+nums[k]==0:
                            triplets.append(([nums[i], nums[j], nums[k]]))
                            k=k-1
                            j=j+1
                            while j<k and nums[j] == nums[j - 1]:
                                j=j+1
                            while j<k and nums[k] == nums[k + 1]:
                                k=k-1
                        elif nums[i]+nums[j]+nums[k]>0:
                            k=k-1
                        else:
                            j=j+1
            i=i+1
        return triplets

            
                    
        