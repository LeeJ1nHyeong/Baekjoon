import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = br.readLine().split(" ");
        int n = Integer.parseInt(inputs[0]);
        int m = Integer.parseInt(inputs[1]);

        int[][] maze = new int[n][m];  // 미로

        for (int i = 0; i < n; i++) {
            inputs = br.readLine().split(" ");
            for (int j = 0; j < m; j++) {
                maze[i][j] = Integer.parseInt(inputs[j]);
            }
        }

        int[][] dp = new int[n + 1][m + 1];  // dp

        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < m + 1; j++) {
                // 현재 위치 인덱스 기준 i - 1 위치와 j - 1 위치 중 최댓값과 현재의 maze 값을 더해서 dp에 저장
                dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]) + maze[i - 1][j - 1];
            }
        }

        System.out.println(dp[n][m]);
    }
}