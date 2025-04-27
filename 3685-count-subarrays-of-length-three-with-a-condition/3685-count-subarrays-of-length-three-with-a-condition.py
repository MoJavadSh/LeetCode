class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        length = len(nums)
        first = 0
        count = 0
        while first+2 < length:
            sum = nums[first] + nums[first+2]
            if sum == (nums[first+1]/2) :
                count += 1
            first += 1
        return count
