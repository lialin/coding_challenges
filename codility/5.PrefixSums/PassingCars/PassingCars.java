/**
 * Author: Liang Lin
 * Email: lianglin@outlook.com
 * Date: 2016-04-01
 */
Class Solution {
    public int solution(int[] A) {
        int counter = 0;
        int eastcar = 0;
        int threshold = 1000000000;
        for (int i = 0; i < A.length; i++) {
            if(A[i] == 0) {
                eastcar ++;
            } else {
                counter += eastcar;
                if(counter > threshold) {
                    return -1;
                }
            }
        }
        return counter;
    }
}
