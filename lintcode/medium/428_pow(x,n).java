public class Solution {
    /**
     * @param x: the base number
     * @param n: the power number
     * @return: the result
     */
    public double myPow(double x, int n) {
        // write your code here
        boolean isNeg = (n < 0);
        if (isNeg){
            x = 1 / x;
            n = - (n + 1); // avoid overflow
        }
        double output = 1, temp = x;
        while (n > 0){
            if (n % 2 == 1){
                output *= temp;
            }
            temp *= temp;
            n = n / 2;
        }
        if (isNeg){
            output *= x;
        }
        return output;
    }
}
