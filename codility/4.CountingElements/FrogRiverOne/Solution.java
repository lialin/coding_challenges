/**
 * Author: Liang Lin
 * Email: lin.lag@gmail.com
 * Date: 2016-03-24
 */
Class Solution {
    public int solution(int X, int[] A) {
        boolean[] B = new boolean[X];
        int counter = 0;
        int n = A.length;
        for(int i=0; i < n; i++) {
            if(A[i] <= X) {
                B[A[i]-1] = true;
                while(B[counter]) {
                    counter ++;
                    if(counter >= X) {
                        return i;
                    }
                }
            }
        }
        return -1;
    }
}
