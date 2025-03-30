#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <math.h>
#include <string.h>
#include <limits.h>
using namespace std;
//기수정렬로 랜덤 int를 정렬해보자 (lrs)
void rsort(vector<int> &v, int length) {	//length : 자릿수
	int size = v.size();
	vector<queue<int>> radix(10);
	for (int i = length; i > 0; i--) {
		for (int j = 0; j < size; j++) {
			radix[v[j] % (int)pow(10, (length - i + 1)) / (int)pow(10, (length - i))].push(v[j]);
		}	//0~9 큐에 기수 넣기
		//큐에 모두 넣었으니 0~9큐 차례대로 꺼내서 배열에 넣어주자
		int progress = 0;	//큐에 있는걸 배열에 넣는 진행도를 저장할 변수
		for (int j = 0; j < 10; j++) {
			while (radix[j].size()) {
				v[progress] = radix[j].front();
				radix[j].pop();
				progress++;
			}
		}
	}
}

int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	srand(time(NULL));
	vector<int> v(100);
	for (int i = 0; i < 100; i++)	//난수 초기화 0 ~ 32768
		v[i] = rand();
	cout << "before sort: ";
	for (int i = 0; i < 100; i++) {
		cout << "[" << v[i] << "] ";
	}
	rsort(v, 5);	//기수정렬 실행
	cout << "\n\nafter sort: ";
	for (int i = 0; i < 100; i++) {
		cout << "[" << v[i] << "] ";
	}
}
