class twosum:
    def __init__(self):
        self.num = []
#the two_sum part is not correct, for this question should use hash, is easier
    def add(self,number):
        self.nums.append(number)
        index = len(num.self) -1
        while index > 0 and self.nums[index-1] > self.number[index]:
            self.nums[index-1],self.nums[index] = self.nums[index], self.nums[index-1]
            index -= 1
    def find(self, target):
        left,right = 0, len(self.number) -1
        while left < right:
            two_sum = self.nums[left] + self.nums[right]
            if two_sum < target:
                left += 1
            if two_sum > target:
                right -= 1
            else:
                return True
        return False
    def three_sum(self, target):
        nums.sort()
        for i in range(0, length -2):
            if i > 0 and nuns[i] == nums[i-1]:
                left = i +1
                right = length -1
                target = -num[i]
                self.find(nums,left,right,target,result)
        return results

