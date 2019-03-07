// This solution is based on the one given in Jiuzhang.com.
public class Solution {
    /**
     * @param matrix: matrix, a list of lists of integers
     * @param target: An integer
     * @return: a boolean, indicate whether matrix contains target
     */
    public boolean searchMatrix(int[][] matrix, int target) {
        // write your code here
        if (matrix == null || matrix.length <= 0 ){
            return false;
        }
        if (matrix[0] == null || matrix[0].length <= 0){
            return false;
        }
        
        int start = 0, end = matrix.length * matrix[0].length - 1;
        int row_len = matrix[0].length;
        while (start + 1 < end){
            int mid = start + (end - start) / 2;
            int number = matrix[mid / row_len][mid % row_len];
            if (number < target){
                start = mid; 
            }
            else if (number == target){
                return true;
            }
            else{
                end = mid;
            }
        }
        return (target == matrix[start / row_len][start % row_len] || target == matrix[end / row_len][end % row_len]);
        
    }
}
