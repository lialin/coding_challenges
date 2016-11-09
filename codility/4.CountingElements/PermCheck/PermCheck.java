/**
 * Author: Liang Lin
 * Email: lianglin@outlook.com
 * Date: 2016-03-26
 */
import java.util.BitSet;
Class Solution {
    public int solution(int[] A) {
        int n = A.length;
        BitSet B = new BitSet(n);
        for(int i=0; i<n; i++) {
            if(A[i]>n || B.get(A[i]-1)) {
                return 0;
            } else {
                B.set(A[i]-1);
            }
        }
        return 1;
    }
}
