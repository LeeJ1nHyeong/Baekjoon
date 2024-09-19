import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String s = br.readLine();
        StringTokenizer st = new StringTokenizer(s);

        int n = Integer.parseInt(st.nextToken());
        long m = Integer.parseInt(st.nextToken());

        long[] times = new long[n];

        for (int i = 0; i < n; i++) {
            long t = Integer.parseInt(br.readLine());
            times[i] = t;
        }

        // 각 심사대의 심사 시간을 오름차순으로 정렬
        Arrays.sort(times);

        long ans = 0;
        long left = 1;  // 왼쪽 포인터
        long right = times[n - 1] * m;  // 오른쪽 포인터를 심사 시간 최댓값 * 심사 대기자 수로 시작

        // 이분탐색 진행
        while (left <= right) {
            long mid = (left + right) / 2;

            long count = 0;

            // 중간값을 각 심사 시간으로 나눈 몫을 count에 추가
            for (int i = 0; i < n; i++) {
                count += mid / times[i];

                // 오버플로우 방지를 위해 m을 넘기면 for문 중단
                if (count >= m) {
                    break;
                }
            }

            // count가 m보다 크거나 같다면 ans에 mid 저장 후 오른쪽 포인터 값 최신화
            if (count >= m) {
                ans = mid;
                right = mid - 1;
            } else {  // count가 m보다 작다면 왼쪽 포인터 값 최신화
                left = mid + 1;
            }
        }

        System.out.println(ans);
    }
}