#lint code 90   lecture25
def KsumII(self,A,K,target)：
# 用sort 方便去重
    A.sort()
    subsets = []
    self.dfs(A,0,target,[],subsets)
    return subsets

#  递归的定义 从index开始，选K的数字放入subset，满足K个的数字和是target
def dfs(self,A,index,k,target,subset,subsets):
    if k ==0 and target == 0:
        subset.append(list(subset))
        return
    
    if k ==0 or target <= 0:
        return
# 递归的拆解
    for i in range (index,len(A)):
        subset.append(A[i])
        self.dfs(A,i+1,k-1,target - A[i],subset,subsets)
        subset.pop()




