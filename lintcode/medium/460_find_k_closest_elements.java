/*
This is my own implementation.
*/
public class Solution {
    /**
     * @param A: an integer array
     * @param target: An integer
     * @param k: An integer
     * @return: an integer array
     */
    public int[] kClosestNumbers(int[] A, int target, int k) {
        // write your code here
        
        int[] outputList = new int[k];
        if (k <= 0 || A.length <= 0){
            return outputList;
        }
        int indToChoose = getClosestInd(A, target);
        outputList[0] = A[indToChoose];
        int nextIndToFill = 1;
        int left = indToChoose, right = indToChoose;
        while (nextIndToFill < k){
            int leftValue = Integer.MAX_VALUE;
            int rightValue = Integer.MAX_VALUE;
            if (left > 0){
                leftValue = A[left - 1];
            }
            if (right < A.length - 1){
                rightValue = A[right + 1];
            }
            if (Math.abs(leftValue - target) <= Math.abs(rightValue - target)){
                outputList[nextIndToFill] = leftValue;
                left--;
            }
            else{
                outputList[nextIndToFill] = rightValue;
                right++;
            }
            nextIndToFill++;
        }
        return outputList;
         
    }
    
    public int getClosestInd(int[] A, int target){
        int start = 0, end = A.length - 1;
        while (start + 1 < end){
            int mid = start + (end - start) / 2;
            if (A[mid] > target){
                end = mid;
            }
            else if (A[mid] == target){
                end = mid;
            }
            else{
                start = mid;
            }
        }
        if (A[start] == target || Math.abs(A[start] - target) <= Math.abs(A[end] - target)){
            return start;
        }
        if (A[end] == target ||  Math.abs(A[start] - target) > Math.abs(A[end] - target)){
            return end;
        }
        return -1;
    }
}
