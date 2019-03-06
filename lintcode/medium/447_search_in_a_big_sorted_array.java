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


/**
* 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
* - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
* - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
* - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
* - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
*/ 

/////////////// 方法1 倍增

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
        int firstElement = reader.get(0);
        if (firstElement == target) 
            return 0;
        else if (firstElement > target)
            return -1;
        
        int idx = 0, jump = 1;
        while (jump != 0) {
            while (jump != 0 && reader.get(idx + jump) >= target)   // 越界时返回INT_MAX, 必然不小于target
                jump >>= 1;
            idx += jump;
            jump <<= 1;     // 当jump为0时, 左移一位不影响它的值, 不影响循环结束
        }
        
        if (reader.get(idx + 1) == target)
            return idx + 1;
        else
            return -1;
    }
}

/////////////// 方法2 二分

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
        int l = 0, r = 1, mid;
        while (reader.get(r) < target)     // 越界返回INT_MAX, 必然大于target, 所以没有关系
            r <<= 1;
        
        while (l < r) {
            mid = (l + r) >> 1;
            if (reader.get(mid) >= target)
                r = mid;
            else
                l = mid + 1;
        }
        
        if (reader.get(l) == target)
            return l;
        else
            return -1;
    }
}
