class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        nums.sort()
        subsets = [[]]
        indexes = [-1]  # 记录subsets中每个集合结尾元素的下标
        
        for i in range(len(nums)):
            size = len(subsets)
            for s in range(size):
                if i > 0 and nums[i] == nums[i-1] and indexes[s] != i-1:
                    continue  # 去重，如果有重复数字出现，只有前上一个数字选了才能选当前数字
                subsets.append(list(subsets[s]))
                subsets[-1].append(nums[i])
                indexes.append(i)
        
        return subsets

        #需要思考
        