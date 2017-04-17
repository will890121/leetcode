class Solution(object):
    def twoSum(self, nums, target):
        numsLen = len(nums)
        for i in range(numsLen):
            for j in range(i + 1, numsLen):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return False


if __name__ == '__main__':
    print(Solution().twoSum([1, 2, 3, 4, 5, 6], 10))
    print(Solution().twoSum([3, 2, 4], 6))
