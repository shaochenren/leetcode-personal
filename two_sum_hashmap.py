class twosum:
    def __init__(self):
        self.num_to_cnt_map = {}
    def add(self, number):
        self.num_to_cnt_map[number] = self.num_to_cnt_map.get(number,0) +1
    def find(self,target):
        for num1 in self.num_to_cnt_map:
            num2 = target - num1
            num2cnt = 2 if(num1 == num2)else 1
            if self.num_to_cnt_map.get(num2,0) >=num2.cnt:
                return True
        return False 