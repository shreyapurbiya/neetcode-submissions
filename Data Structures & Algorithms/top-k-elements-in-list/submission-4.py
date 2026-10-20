class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = {}
        i=0
        for x in nums:
            if x in mydict:
                mydict[x] = mydict[x]+1
            else:
                mydict[x]= 1
        sorteddict = dict(sorted(mydict.items(), key=lambda item: item[1], reverse=True))
        diff = len(sorteddict)-k
        while i<diff:
            sorteddict.popitem()
            i=i+1
        return(list(sorteddict.keys()))

    
