
class Solution {
    public int solution(int[] A) {
        // write your code in Java SE 8
        int len = A.length;

        for(int i = 0; i < len; i++) {
        	if(A[i] != i+1) {

        		// swap the value of the ith element to the (A[i] - 1)th element
    			// till the value reached the array length
        		while(A[i] != i+1 && A[i] <= len) {
        			swap(A, i);
        		}
        	} 
        }

        // the missing element place will be took by the largest number in the array
        for (int i = 0; i < len; i++) {
        	if(A[i] > len) {
        		return i+1;
        	} 
        }

        return len + 1;
    }

    private void swap(int[] A, int i) {
    	int temp = A[i];
    	int swapIndex = A[i] - 1;
    	A[i] = A[swapIndex];
    	A[swapIndex] = temp;
    }
}
