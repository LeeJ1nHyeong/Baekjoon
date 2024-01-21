import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double totalGrade = 0;
        double totalCredit = 0;

        for (int i = 0; i < 20; i++) {
            String subjectName = sc.next();
            double subjectCredit = sc.nextDouble();
            String subjectGrade = sc.next();

            if (subjectGrade.equals("P")) {  // 평점이 P라면 continue
                continue;
            } else {
                totalCredit += subjectCredit;
                if (subjectGrade.equals("A+")) {
                    totalGrade += subjectCredit * 4.5;
                } else if (subjectGrade.equals("A0")) {
                    totalGrade += subjectCredit * 4.0;
                } else if (subjectGrade.equals("B+")) {
                    totalGrade += subjectCredit * 3.5;
                } else if (subjectGrade.equals("B0")) {
                    totalGrade += subjectCredit * 3.0;
                } else if (subjectGrade.equals("C+")) {
                    totalGrade += subjectCredit * 2.5;
                } else if (subjectGrade.equals("C0")) {
                    totalGrade += subjectCredit * 2.0;
                } else if (subjectGrade.equals("D+")) {
                    totalGrade += subjectCredit * 1.5;
                } else if (subjectGrade.equals("D0")) {
                    totalGrade += subjectCredit * 1.0;
                }
            }

        }

        double grade = totalGrade / totalCredit;
        System.out.printf("%.6f", grade);  // 문제 조건에 맞게 소수점 6자리로 출력
    }
}