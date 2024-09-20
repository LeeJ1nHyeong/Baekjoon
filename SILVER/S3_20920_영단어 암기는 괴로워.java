import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String s = br.readLine();
        StringTokenizer st = new StringTokenizer(s);
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        
        Map<String, Integer> hash = new HashMap<>();  // 단어장

        for (int i = 0; i < n; i++) {
            s = br.readLine();

            // 길이 m 미만의 단어는 단어장 미추가
            if (s.length() < m) {
                continue;
            }

            hash.put(s, hash.getOrDefault(s, 0) + 1);
        }

        // key만 추출하여 리스트 생성
        List<String> keyList = new ArrayList<>(hash.keySet());

        // 자주 나오는 단어, 개수가 같다면 길이 내림차순, 길이가 같다면 알파벳 사전 순으로 정렬
        Collections.sort(keyList, (a, b) -> hash.get(a) == hash.get(b) ?  (a.length() == b.length() ? a.compareTo(b) : b.length() - a.length()) : (hash.get(b) - hash.get(a)));

        // 정렬 후 형식에 맞게 단어 출력
        for (String key : keyList) {
            sb.append(key).append("\n");
        }

        System.out.println(sb);
    }
}