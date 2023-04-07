#二分法算法 默写  time The time complexity of Binary Search Algorithm is O(logN) (Where n is the number of elements in the sorted linear array.)
def binarysearch(self,num,start,end,target):
    mid = (start+end)//2
    if start >=end:
        return False #(sometimes return start, sometimes return end)
    if num[mid] == target:
        return mid
    if target > num[mid]:
        return binarysearch(self,num,mid+1,end,target)
    else:
        return binarysearch(self,num,start,mid+1,target)
    # if we use two function, we need to return something here

    
