def rerange(self,A):
    neg_count = self.partation(A)
    pos_count = self.len(A)-neg_count
    left = 1 if neg_count > pos_count else 0
    right = len(A) -(2 if pos_cnt > neg_cnt else 1)
def partation(self,A):
    left, right = 0, len(A)-1
    while left <= right:
        while left <=right and A[left] < 0:
            left +=1
        while left < right and A[right] > 0:
            right -=1
            if left <=right:
                A[left],A[right] = A[right], A[left]
                left+=1
                right-=1
        return left
def interleave(self,A,left,right):
    while left< right:
        A[left],A[right] = A[right],A[left]
        left +=2
        right -=2
