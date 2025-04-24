#include <iostream>
#include <queue>
using namespace std;


int main(void) {
    
    int t;
    cin >> t;

    // 오버플로우 방지를 위해 long long으로 변수 타입 설정
    for (int i = 0; i < t; i++)
    {
        priority_queue<long long, vector<long long>, greater<long long>> pq;
        int n;
        cin >> n;
        long long ans = 0;

        for (int j = 0; j < n; j++)
        {
            int card;
            cin >> card;
            pq.push(card);
        }

        while (pq.size() > 1) {
            long long num1 = pq.top();
            pq.pop();
            long long num2 = pq.top();
            pq.pop();

            long long sum = num1 + num2;
            pq.push(sum);

            ans += sum;
        }

        cout << ans << "\n";
    }

    
    return 0;
}