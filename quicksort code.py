def quicksort(int A[], int start int right){
int left = start, left  = end
int piviot = [A(start + end)]/2
while (left<= right){
    while(left <=right and A[left] < pivot){
        left -= 1;
    }
    while(left <=right and A[right] > pivot){
        right -= 1;
    }
    if(left <=right){
        int temp = A[left];
        A[left] = A[right];
        A[right] = temp;
        left -=1;
        right -=1;
    }
    quicksort(a,start,right)
    quicksort(a,left,end)
}
}