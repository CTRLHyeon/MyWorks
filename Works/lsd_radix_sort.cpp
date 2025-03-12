#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <math.h>
#include <string.h>
#include <limits.h>
using namespace std;
//������ķ� ���� int�� �����غ��� (lrs)

void rsort(vector<int> &v, int length) {	//length : �ڸ���
	int size = v.size();
	vector<queue<int>> radix(10);
	for (int i = length; i > 0; i--) {
		for (int j = 0; j < size; j++) {
			radix[v[j] % (int)pow(10, (length - i + 1)) / (int)pow(10, (length - i))].push(v[j]);
		}	//0~9 ť�� ��� �ֱ�
		//ť�� ��� �־����� 0~9ť ���ʴ�� ������ �迭�� �־�����
		int progress = 0;	//ť�� �ִ°� �迭�� �ִ� ���൵�� ������ ����
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
	for (int i = 0; i < 100; i++)	//���� �ʱ�ȭ 0 ~ 32768
		v[i] = rand();
	cout << "before sort: ";
	for (int i = 0; i < 100; i++) {
		cout << "[" << v[i] << "] ";
	}

	rsort(v, 5);

	cout << "\n\nafter sort: ";
	for (int i = 0; i < 100; i++) {
		cout << "[" << v[i] << "] ";
	}
}