class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        numOfList = len(nums)
        ansList = [0] * numOfList
        for i in range(0,numOfList):
            if i==0:
                ansList[i] = nums[i]
            elif i>0:   #2,3,4...
                ansList[i] = ansList[i-1] + nums[i]
        return ansList
