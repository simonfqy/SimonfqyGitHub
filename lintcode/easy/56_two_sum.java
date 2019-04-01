// This is almost identical copy of the solution provided by Jiuzhang.com.
public class Solution {
    /**
     * @param numbers: An array of Integer
     * @param target: target = numbers[index1] + numbers[index2]
     * @return: [index1, index2] (index1 < index2)
     */
    class Pair {
        Integer value;
        Integer index;
        public Pair(Integer value, Integer index){
            this.value = value;
            this.index = index;
        }
        
        Integer getValue(){
            return this.value;
        }
    }
    
    class ValueComparator implements Comparator<Pair>{
        
        @Override
        public int compare(Pair p1, Pair p2){
            return p1.getValue().compareTo(p2.getValue());
        }
    }
    public int[] twoSum(int[] numbers, int target) {
        // write your code here
        Pair[] valToInd = new Pair[numbers.length];
        for (int i = 0; i < numbers.length; i++){
            valToInd[i] = new Pair(numbers[i], i);
        }
        Arrays.sort(valToInd, new ValueComparator());
        
        int left = 0, right = numbers.length - 1;
        while (left < right){
            if (valToInd[left].getValue() + valToInd[right].getValue() == target){
                int leftInd = valToInd[left].index;
                int rightInd = valToInd[right].index;
                int[] results = {Math.min(leftInd, rightInd), Math.max(leftInd, rightInd)};
                return results;
            }
            if (valToInd[left].getValue() + valToInd[right].getValue() < target){
                left++;
            }
            else{
                right--;
            }
        }
        int[] res = {};
        return res;
    }
}
