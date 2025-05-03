#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <climits>
using namespace std;;


int cow[200001];
pair<int, int> minMaxSegmentTree[800004];

// 최대, 최소 세그먼트 트리 생성
pair<int, int> init(int start, int end, int index) {
	if (start == end) {
		minMaxSegmentTree[index] = { cow[start], cow[start] };
		return minMaxSegmentTree[index];
	}

	int mid = (start + end) / 2;
	pair<int, int> left = init(start, mid, index * 2);
	pair<int, int> right = init(mid + 1, end, index * 2 + 1);

	int maxValue = max(left.first, right.first);
	int minValue = min(left.second, right.second);
	
	minMaxSegmentTree[index] = { maxValue, minValue };
	return minMaxSegmentTree[index];
}

// 구간별 최대 최소값 구하기
pair<int, int> getMaxMin(int start, int end, int index, int left, int right) {
	if (left > end or right < start) return { 0, INT_MAX };
	if (left <= start and end <= right) return minMaxSegmentTree[index];

	int mid = (start + end) / 2;
	pair<int, int> l = getMaxMin(start, mid, index * 2, left, right);
	pair<int, int> r = getMaxMin(mid + 1, end, index * 2 + 1, left, right);

	int maxValue = max(l.first, r.first);
	int minValue = min(l.second, r.second);
	return { maxValue, minValue };
}


int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	int n, q;
	cin >> n >> q;

	for (int i = 1; i <= n; i++)
	{
		cin >> cow[i];
	}

	init(1, n, 1);

	while (q--) {
		int a, b;
		cin >> a >> b;

		pair<int, int> maxMin = getMaxMin(1, n, 1, a, b);

		cout << maxMin.first - maxMin.second << "\n";
	}

	return 0;
}