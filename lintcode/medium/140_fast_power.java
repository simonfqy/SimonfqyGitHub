/**
* 本参考程序来自九章算法，由 @九章管理员 提供。版权所有，转发请注明出处。
* - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
* - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
* - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
* - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
*/ 

public class Solution {
    /**
     * @param a: A 32bit integer
     * @param b: A 32bit integer
     * @param n: A 32bit integer
     * @return: An integer
     */
    public int fastPower(int a, int b, int n) {
        // This long type is crucial. If set to int will cause problems.
        long ans = 1, tmp = a;
        
        while (n != 0) {
            if (n % 2 == 1) {
                ans = (ans * tmp) % b;
            }
            tmp = (tmp * tmp) % b;
            n = n / 2;
        }
        
        return (int) ans % b;
    }
}


// My own solution.
public class Solution {
    /**
     * @param a: A 32bit integer
     * @param b: A 32bit integer
     * @param n: A 32bit integer
     * @return: An integer
     */
    public int fastPower(int a, int b, int n) {
        // write your code here
        if (n == 0){
            return (1 % b);
        }
        if (n == 1){
            return (a % b);
        }
        long temp = 0;
        if (n % 2 == 1){
            temp = fastPower(a, b, (n-1)/2);
            return (int) ((((temp * temp) % b) * a) % b);
        }
        else{
            temp = fastPower(a, b, n/2);
            // It is extremely important to wrap it in suitable brackets. The modulo operator
            // has a pretty low precedence.
            return (int) ((temp * temp) % b);
        }
    }
}

// My own iterative solution.
public class Solution {
    /**
     * @param a: A 32bit integer
     * @param b: A 32bit integer
     * @param n: A 32bit integer
     * @return: An integer
     */
    public int fastPower(int a, int b, int n) {
        // write your code here
        long ans = 1;
        long base = a;
        while (n > 0){
            if (n % 2 == 1){
                ans = (ans * base) % b;
            }
            base = (base * base) % b;
            n = n / 2;
        }        
        return (int) (ans % b);
    }
}
