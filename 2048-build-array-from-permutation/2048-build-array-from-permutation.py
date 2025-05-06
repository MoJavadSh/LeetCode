class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(0,len(nums)):
            ind = nums[i]
            ans.append(nums[ind])

        return ans