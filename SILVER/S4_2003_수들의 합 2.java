import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] numbers = new int[n];

        for (int i = 0; i < n; i++) {
            int a = sc.nextInt();
            numbers[i] = a;
        }

        int i = 0, j = 0;  // 투 포인터로 사용할 i, j
        int ans = 0;
        int sum = 0;
        sum += numbers[0];  // 수열의 첫번째 항을 더한 상태로 시작

        while (i < n) {
            // j가 끝까지 도달한 상태에서 수열 합이 m 미만이면 break
            if (j == n - 1 && sum < m) {
                break;
            }

            // 수열 합이 m 미만이라면 j가 마지막 인덱스일 경우를 제외하고 1 증가한 후 수열 합에 해당 인덱스 값 더하기
            if (sum < m) {
                if (j < n - 1) {
                    sum += numbers[++j];
                }
            } else {
                // 수열 합이 m일 경우 ans 1 증가,
                // 이 후 i 인덱스 값을 빼준 뒤 i 1 증가
                // 마찬가지로 j가 마지막 인덱스인 경우를 제외하고 j 1 증가 후 수열 합에 해당 인덱스 값 더해주기
                if (sum == m) {
                    ans++;
                    sum -= numbers[i++];
                    if (j < n - 1) {
                        sum += numbers[++j];
                    }
                } else {  // 수열 합이 m을 넘을 경우 i 인덱스 값을 빼준 후 i 1 증가
                    sum -= numbers[i++];
                }
            }
        }

        System.out.println(ans);
    }
}