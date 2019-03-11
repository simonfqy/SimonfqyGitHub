'''
Link: https://www.lintcode.com/problem/fast-power/description
'''

# This is my own recursive solution. Won't get stack overflow error.
class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
        # Try recursive version
        if n <= 1:
            return int(pow(a, n) % b)
        if n % 2 == 1:
            return int(((a % b) * pow(self.fastPower(a, b, (n - 1) / 2), 2)) % b)
        else:
            return int((pow(self.fastPower(a, b, n/2), 2)) % b)
      
    
# My own non-recursive solution.
class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
        # Try non-recursive version
        if n == 0:
            return int(1 % b)
        ret_value = int(a % b)
        n -= 1
        while n > 0:
            exponent = 1
            inner_mod = int(a % b)
            while exponent <= n / 2:
                inner_mod = int(pow(inner_mod, 2) % b)
                exponent *= 2
            ret_value = int((inner_mod * (ret_value % b)) % b)
            n -= exponent
        return ret_value
    
    
# 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code

class Solution:
    """
    @param a, b, n: 32bit integers
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # a ^ n % b
        # 比如 n=5,可以看做 a^(101)2 % b （5的二进制是101）
        # 拆开也就是 [a^(100)2 * a&(1)2] % b
        # 因此相当于我们把 n 做二进制转换，碰到 1 的时候，乘一下对应的 a 的幂次
        # 而 a 的幂次我们只需要知道 a^1, a^(10)2, a^(100)2 ... 也就是 a^1, a^2, a^4 ...
        # 因此不断的把 a = a * a 就可以了
        # 中间计算的时候，随时可以 % b 避免 overflow 其不影响结果，这是 % 运算的特性。
        ans = 1
        while n > 0:
            if n % 2 == 1:
                ans = (ans * a) % b
            a = a * a % b
            n = n // 2
        return ans % b
