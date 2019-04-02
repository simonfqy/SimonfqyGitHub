public class Solution {
    /**
     * @param nums: an array of integers
     * @return: the number of unique integers
     */
    public int deduplication(int[] nums) {
        // write your code here
        int n = nums.length;
        if (n == 0){
            return 0;
        }
        Arrays.sort(nums);
        int left = 1;
        for (int i = 1; i < n; i++){
            if (nums[i] != nums[i - 1]){
                nums[left] = nums[i];
                left++;
            }
        }
        return left;
    }
}
