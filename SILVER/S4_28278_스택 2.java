import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        StringTokenizer st;
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            st = new StringTokenizer(s);

            int command = Integer.parseInt(st.nextToken());

            switch (command) {
                // 스택에 숫자 삽입
                case 1:
                    int num = Integer.parseInt(st.nextToken());
                    stack.push(num);
                    break;

                // 스택의 가장 위에 있는 정수를 pop하고 출력
                case 2:
                    // 비어있다면 -1 출력
                    if (stack.empty()) {
                        sb.append(-1).append("\n");
                    } else {
                        sb.append(stack.pop()).append("\n");
                    }
                    break;

                // 스택에 들어있는 정수 개수
                case 3:
                    sb.append(stack.size()).append("\n");
                    break;

                // 스택이 비어있다면 1, 아니면 0 출력
                case 4:
                    if (stack.empty()) {
                        sb.append(1).append("\n");
                    } else {
                        sb.append(0).append("\n");
                    }
                    break;

                // 스택의 가장 위에 있는 정수를 pop하지 않고 출력
                case 5:
                    // 비어있다면 -1 출력
                    if (stack.empty()) {
                        sb.append(-1).append("\n");
                    } else {
                        sb.append(stack.peek()).append("\n");
                    }
                    break;
            }
        }

        System.out.println(sb);
    }
}