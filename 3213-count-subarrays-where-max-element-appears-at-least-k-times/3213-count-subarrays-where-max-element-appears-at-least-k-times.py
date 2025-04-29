class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        count = 0
        left = 0
        count_max = 0
        n = len(nums)

        for right in range(n):
            if nums[right] == max_val:
                count_max += 1

            while count_max >= k:
                count += n - right
                if nums[left] == max_val:
                    count_max -= 1
                left += 1

        return count