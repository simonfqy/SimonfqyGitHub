public class Solution {
    /**
     * @param n: an integer
     * @return: an ineger f(n)
     */
    public int fibonacci(int n) {
        // write your code here
        int first = 0;
        int second = 1; 
        int third = 0;
        if (n == 1)
            return first;
        if (n == 2){
            return second;
        }
        for (int i = 3; i <= n; i++){
            third = first + second;
            first = second;
            second = third;
        }
        return third;        
    }
}
