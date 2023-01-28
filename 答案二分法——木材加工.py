#183
def woodcut(self, L,K):
    if not L:
        return -1
    start, end = 1,min(max(L),sum(L)//K)
    mid = (start + end) //2
    if end <1:
        return 0
    while start + 1 < end:
        if self.get_count(L.min) >=K:
            start = end
        else:
            end = mid
        return end if self.get_count(L,end) >=k else start
def get_count(self,length):
    return sum(l//length for l in L)

