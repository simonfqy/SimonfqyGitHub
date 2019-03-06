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


// This is my own implementation after the solution from Jiuzhang.com.
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
        int left = getLowerClosest(A, target);
        int right = left + 1;
        for (int i = 0; i < k; i++){
            if (isLeftCloser(A, left, right, target)){
                outputList[i] = A[left];
                left--;
            }
            else{
                outputList[i] = A[right];
                right++;
            }
        }
        return outputList;
    }
    
    public int getLowerClosest(int[] A, int target){
        int start = 0, end = A.length - 1;
        while (start + 1 < end){
            int mid = start + (end - start) / 2;
            if (A[mid] <= target){
                start = mid;
            }
            else{
                end = mid;
            }
        }
        if (A[end] <= target){
            return end;
        }
        if (A[start] <= target){
            return start;
        }
        return -1;
    }
    
    public boolean isLeftCloser(int[] A, int left, int right, int target){
        if (left < 0){
            return false;
        }
        if (right >= A.length){
            return true;
        }
        return target - A[left] <= A[right] - target;
    }
}
