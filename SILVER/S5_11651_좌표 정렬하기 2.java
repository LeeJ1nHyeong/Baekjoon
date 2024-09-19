import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        int[][] point = new int[n][2];

        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            StringTokenizer st = new StringTokenizer(s);

            point[i][0] = Integer.parseInt(st.nextToken());
            point[i][1] = Integer.parseInt(st.nextToken());
        }

        // y좌표 오름차순, y좌표가 같다면 x좌표 오름차순으로 정렬 진행
        Arrays.sort(point, (a, b) -> a[1] == b[1] ? a[0] - b[0] : a[1] - b[1]);

        // 형식에 맞게 출력
        for (int i = 0; i < n; i++) {
            sb.append(point[i][0]).append(' ').append(point[i][1]);
            sb.append('\n');
        }

        System.out.println(sb);
    }
}