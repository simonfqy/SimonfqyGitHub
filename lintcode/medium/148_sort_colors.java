// Important lesson: go step by step, one step at a time.
public class Solution {
    /**
     * @param nums: A list of integer which is 0, 1 or 2 
     * @return: nothing
     */
    public void sortColors(int[] nums) {
        // write your code here
        if (nums.length < 1){
            return;
        }
        int left = 0, middle = 0, right = nums.length - 1;
        // This condition is important. If we remove the = sign from <=, it will cause problems.
        // Basically only those < middle and > right are confirmed
        while (middle <= right){
            if (nums[middle] == 0){
                int temp = nums[middle];
                nums[middle] = nums[left];
                nums[left] = temp;
                left++;
                middle++;
            }
            // If we remove the "else", it will cause problems. So we should do only one thing in
            // one iteration of the loop if we are not completely sure of what we are doing.
            else if (nums[middle] == 2){
                int temp = nums[middle];
                nums[middle] = nums[right];
                nums[right] = temp;
                // We need to consider the edge case carefully. The swapped element from the right
                // pointer could be 0, 1 or 2, so we need to check whether it should be further swapped
                // in the next iteration, so we can't have middle++ here. While for the previous if
                // block where we decide whether nums[middle] == 0, it is guaranteed that the swapped
                // number originally pointed to by left pointer is either 0 or 1, the requirement will
                // always be satisfied, so we can have middle++ there.
                right--;
                
            }
            else{
                middle++;
            }
        }
    }
}
