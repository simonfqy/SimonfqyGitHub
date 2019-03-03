/*This implementation is based on the solution given in Jiuzhang.com*/

public class Solution {
    /**
     * @param s: A string
     * @return: Whether the string is a valid palindrome
     */
    public boolean isPalindrome(String s) {
        // write your code here
        if (s == null)
            return false;
        int left = 0;
        int right = s.length() - 1;
        while (left <= right){
            while (left < right && !Character.isLetterOrDigit(s.charAt(left))){
                left++;
            }
            while (left < right && !Character.isLetterOrDigit(s.charAt(right))){
                right--;
            }
            if (left <= right && Character.toLowerCase(s.charAt(right)) != Character.toLowerCase(s.charAt(left))){
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
