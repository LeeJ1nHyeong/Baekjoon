import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        for (int test = 0; test < t; test++) {
            int n = Integer.parseInt(br.readLine());
            int[] candy = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            int cycle = 0;
            while (true) {
                if (checkCandy(candy)) {
                    break;
                }

                int[] nextCandy = new int[n];

                for (int i = 0; i < n; i++) {
                    if (candy[i] % 2 != 0) {
                        candy[i]++;
                    }
                }

                if (checkCandy(candy)) {
                    break;
                }

                for (int i = 0; i < n; i++) {
                    nextCandy[(i + 1) % n] += candy[i] / 2;
                    nextCandy[i] += candy[i] / 2;
                }

                candy = nextCandy;
                cycle++;
            }

            System.out.println(cycle);
        }
    }

    private static boolean checkCandy(int[] candy) {
        int first = candy[0];

        for (int c : candy) {
            if (c != first) {
                return false;
            }
        }
        return true;

    }
}