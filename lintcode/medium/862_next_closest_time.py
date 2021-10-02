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
    
    
# My own solution. Enumerates all the minutes succeeding the input time and return the one whose digits are all present in 
# the supplied time. It is ugly, but the problem size is small, so it is still efficient.
class Solution:
    """
    @param time: the given time
    @return: the next closest time
    """
    def nextClosestTime(self, time):
        digits = time[:2] + time[3:]
        digit_set = set([digit for digit in digits])
        prev_time = time
        while True:
            minute = int(prev_time[3:])
            if minute < 59:
                minute += 1
                next_min = prev_time[:3] + self.format_number(minute)
            else:
                hour = int(prev_time[:2])
                if hour < 23:
                    hour += 1
                    next_min = self.format_number(hour) + ":00"
                else:
                    next_min = "00:00"
            next_moment_number_only = next_min[:2] + next_min[3:]
            all_digits_exist = all([char in digit_set for char in next_moment_number_only])
            if all_digits_exist:
                return next_min                
            prev_time = next_min

    def format_number(self, number):
        num_str = str(number)
        if len(num_str) < 2:
            num_str = "0" + num_str
        return num_str
    
    
# Answer from a student in jiuzhang.com. Though this solution is highly specific to this problem
# and cannot be generalized to other problems, it is very elegant and succinct.
class Solution:
    """
    @param time: the given time
    @return: the next closest time
    """
    def nextClosestTime(self, time):
        hour, minute = time.split(":")
        curr_min = int(hour) * 60 + int(minute)
        # Using 1441 rather than 1440 for the edge case of the exact same minute (of the next day)
        # being the next closes time. An example is 11:11.
        for i in range(curr_min + 1, curr_min + 1441):
            min_in_day = i % 1440
            h, m = min_in_day // 60, min_in_day % 60
            curr_time_str = "%02d:%02d" % (h, m)
            # The characters comprising of curr_time_str is a subset of those comprising time, so
            # curr_time_str is constructed by reusing the same digits. 
            if set(curr_time_str) <= set(time):
                return curr_time_str
