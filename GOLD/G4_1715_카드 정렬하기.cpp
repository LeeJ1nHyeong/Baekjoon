#include <iostream>
#include <queue>
using namespace std;

priority_queue<int, vector<int>, greater<>> pq;


int main(void) {

    int n;
    int ans = 0;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        int card;
        cin >> card;
        pq.push(card);
    }

    while (pq.size() > 1) {
        int num1 = pq.top();
        pq.pop();
        int num2 = pq.top();
        pq.pop();

        int sum = num1 + num2;
        pq.push(sum);

        ans += sum;
    }

    cout << ans;
    
    return 0;
}