import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        HashSet<String> set = new HashSet<>();
        String s;
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        // 집합에 회사원 이름 저장
        for (int i = 0; i < n; i++) {
            s = br.readLine();
            st = new StringTokenizer(s);

            String name = st.nextToken();
            String enterLeave = st.nextToken();

            // 출근이면 추가, 퇴근이면 삭제
            if (enterLeave.equals("enter")) {
                set.add(name);
            } else {
                set.remove(name);
            }
        }

        // 집합을 리스트로 변환 후 내림차순 정렬
        List<String> setList = new ArrayList<>(set);
        Collections.sort(setList, Collections.reverseOrder());

        // 내림차순 정렬한 이름을 형식에 맞게 출력
        for (String sl : setList) {
            sb.append(sl).append("\n");
        }
        System.out.println(sb);

    }
}