'''
https://www.lintcode.com/problem/strstr-ii/description
This is an extended version of the strstr question in the easy category. A solution is here:
https://github.com/simonfqy/SimonfqyGitHub/blob/36bf717fbb3a3a7e9bca2883f5d1759941cdc9f6/lintcode/easy/13_implement_strstr().py#L5
This version requires that the time complexity is O(n+m), where n is the length of the source string, m is the length of the target.
This implementation uses Rabin-Karp algorithm. Basically it uses hash function.
'''

class Solution:
    """
    @param: source: A source string
    @param: target: A target string
    @return: An integer as index
    """
    def strStr2(self, source, target):
        # write your code here
        if source is None or target is None:
            return -1
        if target == "":
            return 0
        prime = 101 # Changing this number can actually affect the performance.
        BASE = 999983
        n = len(source)
        m = len(target)
        
        target_code = 0
        for i in range(m):
            target_code = (target_code * prime + ord(target[i])) % BASE
        
        power = (prime ** m) % BASE
        source_code = 0
        
        for i in range(n):
            source_code = (source_code * prime + ord(source[i])) % BASE
            if i < m - 1:
                # Not possible to have a match yet, continue
                continue
            
            # Take the old characters out of the window.
            if i >= m:
                source_code = (source_code - ord(source[i - m]) * power) % BASE
            
            if source_code == target_code and source[i - m + 1 : i + 1] == target:
                return i - m + 1
        return -1
