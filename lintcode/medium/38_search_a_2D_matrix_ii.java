// This solution is based on the one given in Jiuzhang.com.
public class Solution {
    /**
     * @param matrix: A list of lists of integers
     * @param target: An integer you want to search in matrix
     * @return: An integer indicate the total occurrence of target in the given matrix
     */
    public int searchMatrix(int[][] matrix, int target) {
        // write your code here
        int occurrence = 0;
        if (matrix == null || matrix.length == 0){
            return occurrence;
        }
        if (matrix[0] == null || matrix[0].length == 0){
            return occurrence;
        }
        int row = matrix.length - 1, col = 0;
        while (row >= 0 && col < matrix[0].length){
            if (matrix[row][col] == target){
                occurrence++;
                row--;
                col++;
            }
            else if (matrix[row][col] > target){
                row--;
            }
            else{
                col++;
            }
        }
        return occurrence;
    }
}
