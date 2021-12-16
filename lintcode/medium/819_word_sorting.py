'''
https://www.lintcode.com/problem/819
'''

# My own solution. Uses 2 dictionaries: 1 maps orthodox letter to unorthodox, another one the other way around.
# Has O(n) time complexity, where n is the total number of letters in the words array.
class Solution:
    """
    @param alphabet: the new alphabet
    @param words: the original string array
    @return: the string array after sorting
    """
    def wordSort(self, alphabet, words):
        orthodox_alphabets = "abcdefghijklmnopqrstuvwxyz"
        orthodox_letter_to_unorthodox = {orthodox: unorthodox for (orthodox, unorthodox) in zip(orthodox_alphabets, alphabet)}
        unorthodox_letter_to_orthodox = {unorthodox: orthodox for (orthodox, unorthodox) in zip(orthodox_alphabets, alphabet)}
        orthodox_words_for_ordering = [self.get_word_for_ordering(word, unorthodox_letter_to_orthodox) for word in words]
        orthodox_words_for_ordering.sort()
        return [self.get_word_for_ordering(orthodox_word, orthodox_letter_to_unorthodox) for orthodox_word in orthodox_words_for_ordering]

    def get_word_for_ordering(self, word, letter_conversion_dict):
        converted_char_list = [letter_conversion_dict[letter] for letter in word]
        return ''.join(converted_char_list)
      
      
