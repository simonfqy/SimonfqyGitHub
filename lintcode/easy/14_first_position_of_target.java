public class Solution {
    /**
     * @param nums: The integer array.
     * @param target: Target to find.
     * @return: The first position of target. Position starts from 0.
     */
    public int binarySearch(int[] nums, int target) {
        // write your code here
        if (nums == null || nums.length == 0){
            return -1;
        }
        return bin_search_get_ind(nums, 0, nums.length - 1, target);
    }
    
    public int bin_search_get_ind(int[] nums, int start, int end, int target){
        if (end - start <= 1){
            if (nums[start] == target){
                return start;
            }
            if (nums[end] == target){
                return end;
            }
            return -1;
        }
        int mid = start + (end - start) / 2;
        if (nums[mid] > target){
            return bin_search_get_ind(nums, start, mid, target);
        }
        if (nums[mid] == target){
            return bin_search_get_ind(nums, start, mid, target);
        }
        if (nums[mid] < target){
            return bin_search_get_ind(nums, mid, end, target);
        }
        // This line of code is here to only prevent compilation error. It is not useful in practice.
        return -1;
    }
}
