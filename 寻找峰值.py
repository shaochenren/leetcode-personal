# 75
def findpeak(self, A):
    start,end = 1,len(A) -2
    mid = (star + end) //2
    while start + 1 < end:
        if A[mid]< A[mid +1]:
            end = mid
        elif A[mid] < A[mid +1]:
            start = mid
        else:
            return mid
        return end if A[start] <A[end]else start