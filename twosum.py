class twosum:
    def __init__(self):
        self.num = []

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
