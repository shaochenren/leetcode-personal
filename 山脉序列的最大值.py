#585
def binarysearch(self,num,target):
    if not num:
        return -1
    start, end = 0,len(num) -1
    while start +1 < end:
        mid = (start + end)//2
        if num[mid] < num[mid +1]:
            end = mid
        else:
            start = mid
        
    return max(num[start],num[end]) 
