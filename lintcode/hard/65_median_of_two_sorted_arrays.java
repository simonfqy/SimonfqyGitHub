/**
* 本参考程序来自九章算法，由 @令狐冲 提供。版权所有，转发请注明出处。
* - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
* - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
* - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
* - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
*/ 

public class Solution {
    /*
     * @param A: An integer array
     * @param B: An integer array
     * @return: a double whose format is *.5 or *.0
     */
    public double findMedianSortedArrays(int[] A, int[] B) {
        return findMedian(
            new PartialArray(A),
            new PartialArray(B)
        );
    }
    
    private double findMedian(PartialArray A, PartialArray B) {
        while (!A.isEmpty() && !B.isEmpty()) {
            if (A.size() == 1 && B.size() == 1) {
                return (A.getMedian() + B.getMedian()) / 2.0;
            }
            
            PartialArray lowerArr = A;
            int lowerIndex = A.getLowerMedianIndex();
            if (A.getLowerMedian() > B.getLowerMedian()) {
                lowerArr = B;
                lowerIndex = B.getLowerMedianIndex();
            }
            
            PartialArray upperArr = A;
            int upperIndex = A.getUpperMedianIndex();
            if (A.getUpperMedian() < B.getUpperMedian()) {
                upperArr = B;
                upperIndex = B.getUpperMedianIndex();
            }
            
            int numOfRemoved = Math.min(
                lowerArr.getNumOfLower(lowerIndex),
                upperArr.getNumOfUpper(upperIndex)
            );
            
            if (lowerArr.get(lowerIndex) == upperArr.get(upperIndex)) {
                return lowerArr.get(lowerIndex);
            }
            
            lowerArr.removeLower(numOfRemoved);
            upperArr.removeUpper(numOfRemoved);
        }
        
        if (A.isEmpty()) {
            return B.getMedian();
        }
        
        return A.getMedian();
    }
}

class PartialArray {
    int[] arr;
    int start, end;
    
    PartialArray(int[] arr) {
        this.arr = arr;
        this.start = 0;
        this.end = arr.length - 1;
    }
    
    public int getLowerMedian() {
        return arr[(start + end) / 2];
    }
    
    public int getUpperMedian() {
        return arr[(start + end + 1) / 2];
    }
    
    public int getLowerMedianIndex() {
        return (start + end) / 2;
    }
    
    public int getUpperMedianIndex() {
        return (start + end + 1) / 2;
    }
    
    public int size() {
        return end - start + 1;
    }
    
    public double getMedian() {
        return (getUpperMedian() + getLowerMedian()) / 2.0;
    }
    
    public boolean isEmpty() {
        return size() == 0;
    }
    
    public int getNumOfUpper(int index) {
        if (index == end) {
            return 1;
        }
        return end - index;
    }
    
    public int getNumOfLower(int index) {
        if (index == start) {
            return 1;
        }
        return index - start;
    }
    
    public void removeLower(int numOfRemoved) {
        start += numOfRemoved;
    }
    
    public void removeUpper(int numOfRemoved) {
        end -= numOfRemoved;
    }
    
    public int get(int index) {
        return arr[index];
    }
}
