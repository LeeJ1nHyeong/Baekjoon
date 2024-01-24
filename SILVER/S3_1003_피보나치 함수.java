import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        for (int i = 0; i < t; i++) {
            int n = sc.nextInt();
            if (n == 0) {  // n == 0일 경우의 예외처리
                System.out.println(1 + " " + 0);
            } else if (n == 1) {  // n == 1일 경우의 예외처리
                System.out.println(0 + " " + 1);
            } else {  // n이 2 이상일 경우 dp를 활용하여 진행
                int[][] cnts = new int[n + 1][2];
                cnts[0][0] = 1;
                cnts[1][1] = 1;

                for (int j = 2; j < n + 1; j++) {
                    cnts[j][0] = cnts[j - 1][0] + cnts[j - 2][0];
                    cnts[j][1] = cnts[j - 1][1] + cnts[j - 2][1];
                }

                System.out.println(cnts[n][0] + " " + cnts[n][1]);
            }
        }
    }
}