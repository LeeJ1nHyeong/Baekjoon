import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String s = br.readLine();
        StringTokenizer st = new StringTokenizer(s);

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        HashSet<String> set = new HashSet<>();  // 집합

        // 단어 n개를 집합에 추가
        for (int i = 0; i < n; i++) {
            String word = br.readLine();
            set.add(word);
        }

        int count = 0;  // 검사 대상 단어 중 집합에 있는 단어 개수

        // 검사 대상 단어 m개 탐색
        for (int i = 0; i < m; i++) {
            String checkWord = br.readLine();

            // 집합에 단어가 포함되어있다면 count 1 추가
            if (set.contains(checkWord)) {
                count++;
            }
        }

        System.out.println(count);
    }
}