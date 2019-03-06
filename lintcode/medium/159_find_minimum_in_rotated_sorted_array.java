public class Solution {
    /**
     * @param nums: a rotated sorted array
     * @return: the minimum number in the array
     */
    public int findMin(int[] nums) {
        // write your code here
        int firstNum = nums[0];
        if (firstNum < nums[nums.length - 1]){
            return firstNum;
        }
        int start = 0, end = nums.length - 1;
        while (start + 1 < end){
            int mid = start + (end - start) / 2;
            if (nums[mid] > firstNum){
                start = mid;
            }
            else{
                end = mid;
            }
        }
        return Math.min(nums[start], nums[end]);
    }
}
