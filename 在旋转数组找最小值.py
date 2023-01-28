#585 用了两次二分
def binarysearch(self,num,target):
    if not num:
        return -1
    start, end = 0,len(num) -1
    while start +1 < end:
        mid = (start + end)//2
        if num[mid] > num[end]:
            start = mid
        else:
            end = mid
        
    return max(num[start],num[end]) 

    # 只用一次二分也可以做，但是时间复杂度是一样的
