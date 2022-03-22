'''
Link: https://www.lintcode.com/problem/1233
'''

# My own solution. Uses 2 hash maps.
class Solution:
    """
    @param s: 
    @return: return a string
    """
    def frequency_sort(self, s: str) -> str:
        char_to_freq = dict()  
        result = ""      
        for char in s:
            char_to_freq[char] = char_to_freq.get(char, 0) + 1
        freq_to_char_list = self.get_freq_to_sorted_char_list(char_to_freq)
        unique_frequencies = sorted(freq_to_char_list, reverse=True)
        for freq in unique_frequencies:
            char_list = freq_to_char_list[freq]
            for char in char_list:
                result += char * freq
        return result

    def get_freq_to_sorted_char_list(self, char_to_freq):
        freq_to_char_list = dict()
        for char, freq in char_to_freq.items():
            if freq not in freq_to_char_list:
                freq_to_char_list[freq] = []
            freq_to_char_list[freq].append(char)
        for freq, char_list in freq_to_char_list.items():
            freq_to_char_list[freq] = sorted(char_list)
        return freq_to_char_list

