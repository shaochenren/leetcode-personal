class partition:
    def __init__(self):
        self.num = []
    
    def p_array(self,nums,target):
        left = 0
        right = len(self.num) -1
        while left <=right:  
            while left <=right and self.num[left] < target:
                left +=1
            while left <=right and self.num[right] >= target:
                right -=1
            if left <=right:
                self.nums[left], self.num.right = self.num[right],self.num[left]
                left +=1
                right -=1
        return left