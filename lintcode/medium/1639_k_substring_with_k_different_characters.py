'''
Link: https://www.lintcode.com/problem/1639
'''

# My own solution. Uses two pointers, has O(n) time and space complexities. 
class Solution:
    """
    @param stringIn: The original string.
    @param K: The length of substrings.
    @return: return the count of substring of length K and exactly K distinct characters.
    """
    def KSubstring(self, stringIn, K):
        substrings = set()
        n = len(stringIn)
        left, right = 0, 0
        count = 0
        characters_to_pos = dict()
        # right: the next char to be added.
        while right < n:
            # The condition stringIn[left] in characters_to_pos is necessary, because stringIn[left] may not be visited yet.
            if right - left >= K and stringIn[left] in characters_to_pos:
                # First remove the left character.
                del characters_to_pos[stringIn[left]]
                left += 1
            # Try to add the right char.
            char = stringIn[right]
            # Remove the part containing duplicate character.
            if char in characters_to_pos:
                new_left = characters_to_pos[char] + 1
                # All the characters in between must be removed from the dictionary.
                # I initially forgot about removing all of them, only removing stringIn[left].
                for i in range(left, new_left):
                    del characters_to_pos[stringIn[i]]
                left = new_left    
            # Actually adding the right char after removing duplicates.
            characters_to_pos[char] = right
            if right - left == K - 1:
                if stringIn[left : right + 1] not in substrings:
                    substrings.add(stringIn[left : right + 1])
                    count += 1
            right += 1         

        return count
            
