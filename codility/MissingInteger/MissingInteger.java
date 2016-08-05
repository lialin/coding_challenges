/**
 * Author: Liang Lin
 * Email: lianglin@outlook.com
 * Date: 2016-03-27
 */
import java.util.BitSet;
Class Solution {
    public int solution(int[] A) {
        int n = A.length;
        BitSet B = new BitSet(n);
        for(int i=0; i<n; i++) {
            if(A[i]>0 && A[i]<=n) {
                B.set(A[i]-1);
            }
        }
        for(int j=0; j<n; j++) {
            if (!B.get(j)) {
                return j+1;
            }
        }
        return n+1;
    }
}
