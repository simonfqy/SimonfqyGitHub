/*
These codes are based on the python implementations. The first code block is using enumeration of central entries, which has
time complexity of O(n^2). The second code block is using Dynamic Programming, also of complexity O(n^2).
*/

public class Solution {
    /**
     * @param s: input string
     * @return: the longest palindromic substring
     */
    private int start;
    private int longest;
    public String longestPalindrome(String s) {
        // write your code here
        if (s == null)
            return "";
        start = 0;
        longest = 0;
        for (int mid = 0; mid < s.length(); mid++){
            getPalindromeString(s, mid, mid);
            getPalindromeString(s, mid, mid + 1);
        }
        return s.substring(start, start + longest);
    }
    
    private void getPalindromeString(String s, int left, int right){
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)){
            left--;
            right++;
        }
        if (longest < right - left - 1){
            longest = right - left - 1;
            start = left + 1;
        }
    } 
}
