/*
My own solution based on the hint given in Jiuzhang.com.
*/
public class Solution {
    /**
     * @param a: the given number
     * @param b: another number
     * @return: the greatest common divisor of two numbers
     */
    public int gcd(int a, int b) {
        // write your code here
        int max = a, min = b;
        if (max < min){
            max = b; 
            min = a;
        }
        if (min != 0){
            return gcd(min, max % min);
        }
        else{
            return max;
        }
    }
}
