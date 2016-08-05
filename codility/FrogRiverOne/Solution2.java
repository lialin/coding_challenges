/**
 * Author: Liang Lin
 * Email: lianglin@outlook.com
 * Date: 2016-03-26
 */
import java.util.BitSet;
Class Solution {
    public int solution(int X, int[] A) {
        //solved using hash table
        int counter = 0;
        int n = A.length;
        BitSet B = new BitSet(X+1);
        for (int i=0; i<n; i++) {
            if(A[i] <= X && !B.get(A[i])) {
                B.set(A[i]);
                counter++;
                if(counter >= X) {
                    return i;
                }
            }
        }
        return -1;
    }
}
