/*This solution was provided by Jiuzhang.com.*/

public class Solution {
    /**
     * @param s: a string which consists of lowercase or uppercase letters
     * @return: the length of the longest palindromes that can be built
     */
    public int longestPalindrome(String s) {
        // write your code here
        Set<Character> set = new HashSet<>();
        for (Character c : s.toCharArray()){
            if (set.contains(c))
                set.remove(c);
            else
                set.add(c);
        }
        int lenRemove = set.size();
        if (lenRemove > 0)
            lenRemove--;
        return s.length() - lenRemove;
    }
}
