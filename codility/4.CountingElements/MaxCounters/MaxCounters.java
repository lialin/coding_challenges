/**
 * Author: Liang Lin
 * Email: lianglin@outlook.com
 * Date: 2016-03-27
 */
 
Class Solution {
    public int solution(int N, int[] A) {
        int mc = 0;
        int lmc = 0;
        int n = A.length;
        int[] B = new int[N];
        for(int i=0; i<n; i++) {
            if(N + 1 == A[i]) {
                lmc = mc;
            } else {
                B[A[i]-1] = Math.max(lmc+1, B[A[i]-1]+1);
                mc = Math.max(mc, B[A[i]-1]);
            }
        }
        int m = B.length;
        for(int j=0; j<m; j++) {
            B[j] = Math.max(lmc, B[j]);
        }
        return B;
    }
}

