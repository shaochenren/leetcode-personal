def binarysearch(self,num,target):
    if not num:
        return -1
    start, end = 0,len(num)
    while start +1 < end:
        mid = (start + end)//2
        if num[mid] < target:
            start = mid
        elif num[mid] == mid:
            end = mid
        else:
            end = mid
    if num[start] == target:
        return start
    if num[end] == target:
        return end
        
    return -1 

