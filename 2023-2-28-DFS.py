# 前中后序遍历 一个binary tree 123456789 

# 前序遍历： 从根开始， 先左便利，之后到右的顺序进行便利 ，根-》左-〉右

#中序遍历 左 根 右  4251637 

# 后序遍历： 左 右 根   4526731

# lint code 425 letter combination of phone number:




#dict
KEYBOARD = {
    '2': 'abc','3': 'def','4': 'ghi','5': 'jkl','6': 'mno','7': 'pqrs','8': 'tuv','9': 'wxyz',
}
#递归的定义
#dight 代表输入的数字
#index 代表当前df处理digit【index】 代表的数字
#combination 代表目前为止得到的组合
#combinations 代表目前为止找到的完整组合
def lettercombination(self,digit):
    if not digit:
        return []
    combinations = []
    self.dfs(self,0,[],combinations)
    return combinations
def dfs(self,digit,index,combination,combinations):
    #递归的出口
    if index == len(digit):
        combinations.append(''.join(combination))
        return
    
    #递归的拆解
    for letter in KEYBOARD[digit[index]]:
        combination.append(letter)
        #继续递归index+1
        self.dfs(digit,index+1,combination,combinations)
        #回溯（backtracking）：把之前加入的字母从combo中移除
        combinations.pop()







