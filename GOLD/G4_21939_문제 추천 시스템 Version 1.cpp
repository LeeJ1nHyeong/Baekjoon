#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <queue>
#include <vector>
using namespace std;

// 문제 구조체
struct Problem {
	int id;
	int difficulty;

    // 어려운 난이도 우선순위 정렬을 위한 operator 재정의
	bool operator<(const Problem& right) const {
		// 문제 난이도 내림차순
		if (difficulty < right.difficulty) return true;
		if (difficulty > right.difficulty) return false;

		// 난이도가 같으면 번호 내림차순
		if (id < right.id) return true;

		return false;
	}
};

// 쉬운 난이도 우선순위 정렬을 위한 cmp
struct cmp {
	bool operator()(const Problem& left, const Problem& right) const {
		if (left.difficulty > right.difficulty) return true;
		if (left.difficulty < right.difficulty) return false;

		// 난이도가 같으면 번호 내림차순
		if (left.id > right.id) return true;

		return false;
	}
};

unordered_map<int, int> um;  // <문제 번호, 난이도>
priority_queue<Problem> problems;  // 문제 난이도 어려운 순서
priority_queue<Problem, vector<Problem>, cmp> reverseProblems;  // 문제 난이도 쉬운 순서


int main() {

	int n;
	cin >> n;

	// 문제 추가
	while (n--) {
		int p, l;
		cin >> p >> l;

		um[p] = l;
		problems.push({ p, l });
		reverseProblems.push({ p, l });

	}

	int m;
	cin >> m;

	// 쿼리 실행
	while (m--) {
		string query;
		cin >> query;

        // 문제 추천
		if (query == "recommend") {
			int x;
			cin >> x;

			switch (x)
			{
			case 1:
				while (true) {
					Problem now = problems.top();
					int id = now.id;
					int difficulty = now.difficulty;

					if (um.find(id) != um.end() and um[id] == difficulty) {
						cout << id << "\n";
						break;
					}

					problems.pop();
				}

				break;

			case -1:
				while (true) {
					Problem now = reverseProblems.top();
					int id = now.id;

					if (um.find(id) != um.end()) {
						cout << id << "\n";
						break;
					}

					reverseProblems.pop();
				}
				break;
			}

		}

        // 문제 추가
		else if (query == "add") {
			int p, l;
			cin >> p >> l;

			um[p] = l;
			problems.push({ p, l });
			reverseProblems.push({ p, l });

		}

        // 문제 제거
		else if (query == "solved") {
			int p;
			cin >> p;

			um.erase(p);
		}
	}

	return 0;
}