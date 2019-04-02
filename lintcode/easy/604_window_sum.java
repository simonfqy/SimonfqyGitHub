public class Solution {
    /**
     * @param nums: a list of integers.
     * @param k: length of window.
     * @return: the sum of the element inside the window at each moving.
     */
    public int[] winSum(int[] nums, int k) {
        // write your code here
        int n = nums.length;
        if (n <= 0){
            return new int [0];
        }
        if (n <= k){
            int[] res = new int [1];
            res[0] = Arrays.stream(nums).sum();
            return res;
        }
        int sum_val = Arrays.stream(nums, 0, k).sum();
        int[] res = new int [n - k + 1];
        res[0] = Arrays.stream(nums, 0, k).sum();
        for (int i = 0; i < res.length - 1; i++){
            res[i + 1] = res[i] - nums[i] + nums[i + k];
        }
        return res;
    }
}
