'''
Link: https://www.lintcode.com/problem/most-common-word/description
'''

# My own solution in Amazon's 2nd round OA. Not exactly the best one.
class Solution:
    """
    @param paragraph: 
    @param banned: 
    @return: nothing
    """
    def mostCommonWord(self, paragraph, banned):
        # 
        n = len(paragraph)
        curr_word = ''
        max_freq = 0
        word_to_freq = dict()
        for i in range(n):
            curr_char = paragraph[i]
            if curr_char.isalpha():
                curr_word += curr_char.lower()
                if i < n - 1:
                    continue
            # I did not notice the case where the curr_word is '' when I was doing Amazon OA.
            if curr_word in banned or curr_word == '':
                curr_word = ''
                continue
            if curr_word not in word_to_freq:
                word_to_freq[curr_word] = 0
            word_to_freq[curr_word] += 1
            curr_freq = word_to_freq[curr_word]
            if curr_freq > max_freq:
                max_freq = curr_freq
            curr_word = ''
        for word, freq in word_to_freq.items():
            if freq == max_freq:
                return word
                      
            
# This solution uses regular expression. Much more powerful than the previous solution.
# 本参考程序来自九章算法，由 @九章算法助教团队 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code

import re
class Solution:
    """
    @param paragraph: 
    @param banned: 
    @return: nothing
    """
    def mostCommonWord(self, paragraph, banned):
        ban = set(banned)
        words = re.findall(r'\w+', paragraph.lower())
        return collections.Counter(w for w in words if w not in ban).most_common(1)[0][0]
    
    
# My own solution based on the previous one.
import re
class Solution:
    """
    @param paragraph: 
    @param banned: 
    @return: nothing
    """
    def mostCommonWord(self, paragraph, banned):
        banned = set(banned)
        words = re.findall(r'\w+', paragraph.lower())
        word_to_freq = dict()
        max_word = None
        max_freq = 0
        for word in words:
            if word in banned:
                continue
            if word not in word_to_freq:
                word_to_freq[word] = 0
            word_to_freq[word] += 1
            if word_to_freq[word] > max_freq:
                max_freq = word_to_freq[word]
                max_word = word
        return max_word
