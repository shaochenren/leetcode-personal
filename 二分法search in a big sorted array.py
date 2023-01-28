# 447 用被增发， 因为end无法取到，所以加倍，然后看是否大于目标值，然后用二分法

def searchsortedarray(self,reader,target):
    range = 1
    while reader.array(range -1) < target:
        range *=2
    start,end =0, range -1
    while start +1 < end:
        mid = (start + end)//2
        if reader.array[mid] < target:
            start = mid
        else:
            end = mid 
    if reader.array[start] == target:
        return start
    if reader.array[end] == target:
        return end        
    return -1 
