import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        for (int i = 0; i < t; i++) {
            int n = sc.nextInt();
            int[] dp = new int[n + 1];  // dp로 풀기 위한 리스트

            // n이 3이하일 경우의 예외처리
            if (n == 1) {
                System.out.println(1);
            } else if (n == 2) {
                System.out.println(2);
            } else if (n == 3) {
                System.out.println(4);
            } else {  // n이 4 이상일 경우 dp로 계산
                dp[1] = 1;
                dp[2] = 2;
                dp[3] = 4;

                for (int j = 4; j < n + 1; j++) {
                    dp[j] = dp[j - 1] + dp[j - 2] + dp[j - 3];
                }
                System.out.println(dp[n]);
            }
        }
    }
}