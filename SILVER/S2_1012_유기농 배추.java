import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String s;
        StringTokenizer st;
        int t = Integer.parseInt(br.readLine());

        int[] dx = {0, 1, 0, -1};
        int[] dy = {1, 0, -1, 0};

        for (int i = 0; i < t; i++) {
            int count = 0;  // 필요한 최소 배추흰지렁이 수

            s = br.readLine();
            st = new StringTokenizer(s);

            int m = Integer.parseInt(st.nextToken());
            int n = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());

            int[][] board = new int[n][m];  // 배추 재배하는 땅
            int[][] visited = new int[n][m];  // 방문 여부 표시

            Queue<int[]> queue = new LinkedList<>();  // 큐

            // 배추의 위치를 board에 표시
            for (int j = 0; j < k; j++) {
                s = br.readLine();
                st = new StringTokenizer(s);

                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());

                board[y][x] = 1;
            }

            for (int x = 0; x < n; x++) {
                for (int y = 0; y < m; y++) {
                    // 배추가 없는 지역이나 방문 지역은 탐색 제외
                    if (board[x][y] == 0) {
                        continue;
                    }
                    if (visited[x][y] == 1) {
                        continue;
                    }

                    // bfs 초기 세팅
                    visited[x][y] = 1;
                    queue.add(new int[]{x, y});

                    // bfs 진행
                    while (!queue.isEmpty()) {
                        int[] current = queue.remove();
                        int cx = current[0];
                        int cy = current[1];

                        // 현재 위치 기준 상하좌우 4방향 탐색
                        for (int d = 0; d < 4; d++) {
                            int nx = cx + dx[d];
                            int ny = cy + dy[d];

                            // 범위를 벗어나면 continue
                            if (nx < 0 || nx == n || ny < 0 || ny == m) {
                                continue;
                            }

                            // 배추가 없는 곳은 continue
                            if (board[nx][ny] == 0) {
                                continue;
                            }

                            // 방문 지역은 continue
                            if (visited[nx][ny] == 1) {
                                continue;
                            }

                            // 조건을 만족하면 방문 표시 후 queue에 좌표 추가
                            visited[nx][ny] = 1;
                            queue.add(new int[]{nx, ny});
                        }
                    }

                    // bfs 종료 후 count 1 추가
                    count++;
                }
            }

            // 배추흰지렁이 수 출력
            System.out.println(count);
        }

    }
}