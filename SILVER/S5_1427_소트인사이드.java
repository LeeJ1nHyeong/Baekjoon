import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        // 숫자를 문자열 리스트로 저장
        String[] s = br.readLine().split("");

        // 내림차순 정렬
        Arrays.sort(s, Collections.reverseOrder());

        for (int i = 0; i < s.length; i++) {
            sb.append(s[i]);
        }

        // 형식에 맞게 출력
        System.out.println(sb);
    }
}