class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        while i<j:
            numsum = numbers[i] + numbers[j]
            if target == numsum:
                return[i+1,j+1]
            elif target < numsum:
                j -=1
            else:
                i +=1



