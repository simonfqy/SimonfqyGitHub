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

// Using dynamic programming.
public class Solution {
    /**
     * @param s: input string
     * @return: the longest palindromic substring
     */
   
    public String longestPalindrome(String s) {
        // write your code here
        if (s == null || s.length() == 0)
            return "";
        int start = 0;
        int longest = 0;
        int n = s.length();
        boolean[][] is_palindrome_tbl = new boolean[n][n];
        for (int i = 0; i < n; i++){
            is_palindrome_tbl[i][i] = true;
            
            if (i < 1){
                continue;
            }
            is_palindrome_tbl[i][i-1] = true;
        }
        longest = 1;
        for (int i = n - 1; i >= 0; i--){
            for (int j = i + 1; j < n; j++){
                if (s.charAt(i) == s.charAt(j) && is_palindrome_tbl[i+1][j-1] == true){
                    is_palindrome_tbl[i][j] = true;
                }
                if (is_palindrome_tbl[i][j] == true && j - i + 1 > longest){
                    longest = j - i + 1;
                    start = i;
                }
            }
        }
        
        return s.substring(start, start + longest);
    }    
}
