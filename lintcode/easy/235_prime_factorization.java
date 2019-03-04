/* This script is written based on the solution in Jiuzhang.com, they are very similar.
*/

public class Solution {
    /**
     * @param num: An integer
     * @return: an integer array
     */
    public List<Integer> primeFactorization(int num) {
        // write your code here
        List<Integer> results = new ArrayList<>();
        int max = (int) Math.sqrt(num);
        for (int i = 2; i <= max && num > 1; i++){
            while (num % i == 0){
                num = num / i;
                results.add(i);
            }
        }
        if (num > 1){
            results.add(num);
        }
        return results;
    }
}
