/*
Link: https://www.lintcode.com/problem/total-occurrence-of-target/description
It is closely related to this question: 
https://github.com/simonfqy/SimonfqyGitHub/blob/7f9f7793b2f89a82f952ddc1becf8483d82361c4/lintcode/medium/61_search_for_a_range.py#L6
*/

// This implementation is my own.
public class Solution {
    /**
     * @param A: A an integer array sorted in ascending order
     * @param target: An integer
     * @return: An integer
     */
    public int totalOccurrence(int[] A, int target) {
        // write your code here
        int occurrence = 0;
        if (A == null || A.length == 0){
            return occurrence;
        }
        // Find the first occurrence.
        int start = 0, end = A.length - 1;
        int firstOccurrence = -1, lastOccurrence = -1;
        while (start + 1 < end){
            int mid = start + (end - start) / 2;
            if (A[mid] < target){
                start = mid;
            }
            else{
                end = mid;
            }
        }
        if (A[start] == target){
            firstOccurrence = start;
        }
        else if (A[end] == target){
            firstOccurrence = end;
        }
        else{
            return occurrence;
        }
        
        start = firstOccurrence; 
        end = A.length - 1;
        while (start + 1 < end){
            int mid = start + (end - start) / 2;
            if (A[mid] > target){
                end = mid;
            }
            else{
                start = mid;
            }
        }
        if (A[end] == target){
            lastOccurrence = end;
        }
        else if (A[start] == target){
            lastOccurrence = start;
        }
        occurrence = lastOccurrence - firstOccurrence + 1;
        return occurrence;
    }
}
