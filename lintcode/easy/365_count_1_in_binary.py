'''
Link: https://www.lintcode.com/problem/count-1-in-binary/description
'''
class Solution:
    """
    @param: num: An integer
    @return: An integer
    """
    def countOnes(self, num):
        # write your code here
        i = 0
        count = 0
        # The integers have unlimited number of digits in Python, so we need to cut it off at 32 binary digits. 
        # If you set it to (1 << i) <= num, it would be incorrect, since there are negative numbers, which has infinite 
        # 1s on the left side.
        while i < 32:
            count += ((1 << i) & num > 0)
            i += 1
        return count
    
    
'''
This solution is from jiuzhang.com.
Q：这为啥可以？
A：其实原理很简单，先说结论：每一次num &= num - 1会使得num最低位1变为0。
例如12，二进制表示为1100，减1后的二进制表示为1011。注意到了吗，减1后，最低位1变成了0，而最低位1后面的0全变成了1，高位不变。
这样和原数按位与后，就只有最低位1发生了变化。所以该过程循环了多少次，就说明抹掉了多少个1。这对于其余正整数也是适用的。

但是要注意的是，Python中的整数是无限长的，负数的二进制表示中会有无限个前导1，因此要先将负数截断至32位。
'''
class Solution:
    def countOnes(self, num):
        if num < 0:
            # Python的整数是无限长的, -1在Java/C++的32位整数中为: 11...11111 (32个1)
            # 但是在Python中为: ...1111111111111 (无限个1)
            # 因此在遇到负数时要先截断为32位
            num &= (1 << 32)-1
        count = 0
        while num != 0:
            num &= num - 1
            count += 1
        return count
