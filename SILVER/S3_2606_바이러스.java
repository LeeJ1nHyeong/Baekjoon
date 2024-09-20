import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String s;
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());

        int[][] board = new int[n + 1][n + 1];
        int[] visited = new int[n + 1];

        int count = 0;

        // 두 컴퓨터 간의 간선을 양방향으로 저장
        for (int i = 0; i < m; i++) {
            s = br.readLine();
            st = new StringTokenizer(s);

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            board[a][b] = 1;
            board[b][a] = 1;
        }

        // bfs 초기 세팅
        Queue<Integer> queue = new LinkedList<>();
        queue.add(1);
        visited[1] = 1;
        
        // bfs 진행
        while (!queue.isEmpty()) {
            int now = queue.remove();

            for (int i = 1; i < n + 1; i++) {
                if (board[now][i] == 0) {
                    continue;
                }

                if (visited[i] == 1) {
                    continue;
                }

                visited[i] = 1;
                count++;
                queue.add(i);
            }
        }

        // 감염된 컴퓨터 수 출력
        System.out.println(count);
    }
}