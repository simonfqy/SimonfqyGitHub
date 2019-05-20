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
