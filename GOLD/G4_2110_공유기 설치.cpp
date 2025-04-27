#include <iostream>
#include <set>
using namespace std;;

int main() {

	int n, c;
	cin >> n >> c;

	set<int> house;

	for (int i = 0; i < n; i++)
	{
		int loc;
		cin >> loc;

		house.insert(loc);
	}

	auto minIter = house.begin();
	auto maxIter = house.end();
	maxIter--;

    // 시작점은 1, 끝점은 두 공유기 간 최대 거리 값
	int start = 1;
	int end = *maxIter - *minIter;

	int ans = 0;

	while (start <= end) {
		int mid = (start + end) / 2;

		int cnt = 1;

		int startLoc = *minIter;
		for (auto iter = ++house.begin(); iter != house.end(); iter++) {
			int nowLoc = *iter;

			if (nowLoc - startLoc >= mid) {
				startLoc = nowLoc;
				cnt++;
			}
		}

		if (cnt >= c) {
			ans = mid;
			start = mid + 1;
		}
		else {
			end = mid - 1;
		}
	}

	cout << ans;

	return 0;
}