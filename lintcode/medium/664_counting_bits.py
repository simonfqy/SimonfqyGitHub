'''
Link: https://www.lintcode.com/problem/counting-bits/description
'''

# Uses Dynamic Programming. The relationship is hard to notice at first, but easy to take advantage of.
class Solution:
    """
    @param num: a non negative integer number
    @return: an array represent the number of 1's in their binary
    """
    def countBits(self, num):
        # write your code here
        answer = [0]
        for i in range(1, num + 1):
            if i % 2 == 0:
                number = answer[i//2]
            else:
                number = answer[i - 1] + 1
            answer.append(number)
        return answer
