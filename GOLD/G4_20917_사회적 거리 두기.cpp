#include <iostream>
#include <algorithm>
using namespace std;;


int main() {
    // 빠른 입출력
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
    //
    
	int t;
	cin >> t;

	while (t--) {
		int n, s;
		cin >> n >> s;

		int loc[200000];

		for (int i = 0; i < n; i++)
		{
			cin >> loc[i];
		}

		sort(loc, loc + n);

		int start = 1;
		int end = loc[n - 1] - loc[0];

		int ans = 0;

		while (start <= end) {
			int mid = (start + end) / 2;

			int cnt = 1;
			int startLoc = loc[0];
			for (int i = 1; i < n; i++)
			{
				int nowLoc = loc[i];

				if (nowLoc - startLoc >= mid) {
					cnt++;
					startLoc = nowLoc;
				}
			}

			if (cnt >= s) {
				ans = mid;
				start = mid + 1;
			}
			else {
				end = mid - 1;
			}
		}

		cout << ans << "\n";
	}

	return 0;
}