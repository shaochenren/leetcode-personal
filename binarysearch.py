use Recursive to do binary search
binary search time complexity is logn

public int find position(int[] nums, int target){
    binarysearch(num, 0, num.length - 1 , target)
}
int binarysearch(int nums, int start, int end, int target){
    if(start > end){
        return -1
    }
    int mid = (start + end)/2
    if(num[mid] == target){ 
        return mid
    }
    if (num[mid] < target){
        binarysearch(int nums, mid+1, end, target)
    }
    return binarysearch(int nums, mid-1, end, target)

}