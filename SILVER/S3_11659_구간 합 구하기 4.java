import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = br.readLine().split(" ");
        int n = Integer.parseInt(inputs[0]);
        int m = Integer.parseInt(inputs[1]);

        int[] numbers = new int[n];

        inputs = br.readLine().split(" ");
        for (int i = 0; i < n; i++) {
            numbers[i] = Integer.parseInt(inputs[i]);
        }

        // dp
        int[] dp = new int[n + 1];

        // 처음부터 i + 1번째 숫자(i번 인덱스)까지의 합을 dp에 저장
        for (int i = 1; i < n + 1; i++) {
            dp[i] = dp[i - 1] + numbers[i - 1];
        }

        // dp를 활용하여 답 출력
        for (int i = 0; i < m; i++) {
            inputs = br.readLine().split(" ");
            int s = Integer.parseInt(inputs[0]);
            int e = Integer.parseInt(inputs[1]);

            int ans = dp[e] - dp[s - 1];
            System.out.println(ans);
        }
    }
}