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


// Solution from Jiuzhang.com. It is unnecessarily complicated since we actually only need set.
public class Solution {
    /**
     * @param nums: an array of integers
     * @return: the number of unique integers
     */
    public int deduplication(int[] nums) {
        // write your code here
        HashMap<Integer, Boolean> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++){
            map.put(nums[i], true);
        }
        int result = 0;
        // Either HashMap.Entry<Integer, Boolean> or Map.Entry<Integer, Boolean> is correct.
        for (HashMap.Entry<Integer, Boolean> entry : map.entrySet()){
            nums[result] = entry.getKey();
            result++;
        }
        return result;
    }
}
