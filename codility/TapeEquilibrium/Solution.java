class Solution {
    public int solution(int[] A) {
        // write your code in Java SE 8
        int result  = 100000;
        int partSum = 0;
        int allSum = 0;
        
        //sum all the array elements 
        for (int i = 0; i < A.length; i++) {
            allSum += A[i];  
        }
        
        //add elements except the last element 
        for (int i = 0; i < A.length-1; i++) {
            partSum += A[i];
            allSum -= A[i];
            result = Math.min(result, Math.abs(partSum - allSum));
        }
        return result;
    }
}