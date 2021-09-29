'''
https://www.lintcode.com/problem/862/
'''

# My own solution. Initially I forgot to replace the later digits with the smallest digit.
class Solution:
    """
    @param time: the given time
    @return: the next closest time
    """
    def nextClosestTime(self, time):
        digits = time[:2] + time[3:]
        smallest_digit = str(min([int(char) for char in digits]))
        sorted_digits = sorted([int(char) for char in digits])
        for i in range(len(time) - 1, -1, -1):
            if i == 2:
                continue
            if i == 4 or i == 1:
                for digit in sorted_digits:
                    if digit > int(time[i]): 
                        if i == 4:
                            return time[:i] + str(digit) + time[i + 1:]
                        if int(digits[0]) < 2 or digit <= 3:
                            return time[:i] + str(digit) + ":" + smallest_digit * 2
            if i == 3:
                for digit in sorted_digits:
                    if digit < 6 and digit > int(time[i]):
                        return time[:i] + str(digit) + smallest_digit
            if i == 0:
                for digit in sorted_digits:
                    if (digit < 2 or (digit == 2 and int(digits[1]) < 4)) and digit > int(time[i]):
                        return str(digit) + smallest_digit + ":" + smallest_digit * 2
        
        return smallest_digit * 2 + ":" + smallest_digit * 2
