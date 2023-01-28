def kclose(self,array, k,target):
    right = self.findupperclosest(array,target)
    left = right -1
    result = []
    for i in range(k):
        if self._isleftcloser(array,target,left,right):
            result.append(array[left])
            left -=1
        else:
            result.append(array[right])
            right+=1
        return result
def isleftcloser(array,target,left,right):
    if left<0:
        return False
    if right ==len(array):
        return True
    return target -array[left] <=array[right] - target


def findupperclosest(self,array,target):
        start, end = 0,len(array) -1
        while start +1 < end:
            mid = (start + end)//2
            if array[mid] < target:
                start = mid
            else:
                start = mid
        if array[start] > target:
            return start
        if array[end] >=target:
            return end
        return len(array)

# time complexity (logn) +(k)