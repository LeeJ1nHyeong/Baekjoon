import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] scores = new int[n];

        for (int i = 0; i < n; i++) {
            int score = Integer.parseInt(br.readLine());
            scores[i] = score;
        }

        int count = 0;

        // 마지막 레벨 점수부터 거꾸로 탐색
        for (int i = n - 1; i > 0; i--) {
            // 현재 레벨 점수가 이전 레벨 점수보다 낮다면
            if (scores[i] <= scores[i - 1]) {
                // 두 점수 차이에 1을 더한 값을 cnt에 추가
                count += scores[i - 1] - scores[i] + 1;

                // 이전 레벨 점수에도 같은 값만큼 차감
                scores[i - 1] -= scores[i - 1] - scores[i] + 1;
            }
        }

        // 점수 변경 횟수 출력
        System.out.println(count);
    }
}