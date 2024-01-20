import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        for (int i = 0; i < t; i++) {
            int n = sc.nextInt();
            // 이 문제를 int 배열로 사용할 경우 int 범위를 벗어나는 값이 생겨 오버플로우 발생
            // long을 이용하여 문제 풀이 진행
            long[] dp = new long[n + 1];

            if (n == 1) {
                System.out.println(1);
            } else if (n == 2) {
                System.out.println(2);
            } else if (n == 3) {
                System.out.println(4);
            } else {
                dp[1] = 1;
                dp[2] = 2;
                dp[3] = 4;

                for (int j = 4; j < n + 1; j++) {
                    dp[j] = (dp[j - 1] + dp[j - 2] + dp[j - 3]) % 1000000009;
                }
                System.out.println((int) dp[n]);
            }
        }
    }
}