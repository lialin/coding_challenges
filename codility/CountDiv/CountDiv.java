/**
 * Author: Liang Lin
 * Email: lianglin@outlook.com
 * Date: 2016-09-14
 */
Class Solution {
    public int solution(int A, int B, int K) {
        int counter = B/K - A/K;
        if(A%K == 0) {
            return counter + 1;
        }
        return counter;
    }
}
