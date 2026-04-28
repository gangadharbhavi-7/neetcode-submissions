class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        isdup=False
        l={}
        for num in nums:
            if num in l:
                l[num]+=1
                isdup=True
                break
            else: 
                l[num]=1
            

        return isdup