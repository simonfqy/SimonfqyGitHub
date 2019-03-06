/**
 * Definition of ArrayReader:
 * 
 * public class ArrayReader {
 * public int get(int index) {
 *          // return the number on given index, 
 *          // return 2147483647 if the index is invalid.
 *     }
 * };
 */
public class Solution {
    /*
     * @param reader: An instance of ArrayReader.
     * @param target: An integer
     * @return: An integer which is the first index of target.
     */
    public int searchBigSortedArray(ArrayReader reader, int target) {
        // write your code here
        if (reader == null){
            return -1;
        }
        int start = 0, gap = 1, end = 1;
        while (reader.get(end) < target){
            start = end;
            end += gap;
            gap += gap;
        }
        while (start + 1 < end){
            int mid = start + (end - start) / 2;
            if (reader.get(mid) >= target){
                end = mid;
            }
            else{
                start = mid;
            }
        }
        if (reader.get(start) == target){
            return start;
        }
        if (reader.get(end) == target){
            return end;
        }
        return -1;
    }
}
