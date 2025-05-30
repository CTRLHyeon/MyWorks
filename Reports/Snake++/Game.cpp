#include <iostream>
#include <conio.h>
#include <vector>
#include <Windows.h>
#include <time.h>
#include "Snake.h"
#define DEFAULT_SPEED 200
using namespace std;

//------------��������-----------------
int width = 30;
int height = 20;
int size = width * height;
double sleep_tick = DEFAULT_SPEED;
int running = 0;
int speed_up = 5;
vector<vector<char>> map(height, vector<char>(width, ' '));
//	#: ��, @: ������ũ �Ӹ�. O: ������ũ ��, A: ���� ����, a: �Ϲ� ����
Snake snake(width, height);
//-----------------------------------

//------------�Լ�����----------------
void init();
void update_map();
void printMap();
void printMain();
void checkCollision();
void food_gen();
void game_speed_increase();
void game();
int play_again();
void clearMap();
void moveCursorHome();
//-----------------------------------

int main() {
	srand(time(NULL));
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
again:

	printMain();
	game();
	if (play_again()) goto again;
	else return 0;
}

//------------�Լ�����----------------

//���� �ʱ� ���� or �ٽ� ����� �ʰ� ������ũ�� �ʱ�ȭ
void init() {
	//map �ʱ�ȭ
	for (int i = 0; i < width; i++) {
		for (int j = 0; j < height; j++) {
			map[j][i] = ' ';
		}
	}
	for (int i = 0; i < width; i++) {
		map[0][i] = '#';
		map[height - 1][i] = '#';
	}
	for (int i = 0; i < height; i++) {
		map[i][0] = '#';
		map[i][width - 1] = '#';
	}

	//snake �ʱ�ȭ
	Snake temp(width, height);
	snake = temp;
	food_gen();
}

//���� ���¸� ������Ʈ �ϴ� �Լ�
//������ũ�� �����̰��ϰ� �浹�� ����. ���� ������ũ�� ��ġ�� �ű�.
void update_map() {
	clearMap();
	snake.move();
	for (auto i : snake.bodyvector())
		if (i.type != '@') map[i.y][i.x] = i.type;
	checkCollision();
	for (auto i : snake.bodyvector()) map[i.y][i.x] = i.type;
}

//�� ���, ���� ��� �Լ�
void printMap() {
	moveCursorHome();
	for (int i = 0; i < height; i++) {
		for (int j = 0; j < width; j++) {
			cout << map[i][j];
		}
		if (i != height - 1) cout << '\n';
		else cout << "\t\t\tScore: " << snake.score();
	}
}

//����ȭ�� ���
void printMain() {
	system("cls");
	for (int i = 0; i < 5; i++) cout << '\n';
	cout << "\t\t\tSnake Game. Press any key to start.";
	_getch();
	system("cls");
}

//������ũ�� �浹 ����
void checkCollision() {
	char current = map[snake.head().first][snake.head().second];
	if (current != ' ' && current != '@') {			//���� �Ӹ��� �ƴҶ�(��򰡿� �浹)
		if (current == 'a') {
			snake.append(1);		//�Ϲݸ���: ���� +1
			food_gen();
		}
		else if (current == 'A') {
			snake.append(3);	//���۸���: ���� +3
			food_gen();
		}
		else running = 0;
	}
}

// �������� ���� ����
void food_gen() {
	int x = rand() % width;
	int y = rand() % height;
	while (map[y][x] != ' ') {
		x = rand() % width;
		y = rand() % height;
	}
	int count = rand() % 100 + 1;
	//25% Ȯ���� ���۸���, 75% Ȯ���� �Ϲ� ����
	if (count > 75) map[y][x] = 'A';
	else map[y][x] = 'a';
}

//����� ���� ���� �ӵ� ����
void game_speed_increase() {
	if (snake.score() - speed_up > 0) {
		sleep_tick *= 0.9;
		speed_up += 5;
	}
}

//������ �������� ������ ����ϴ� �Լ�
void game() {
	running = 1;
	init();
	while (running) {
		if (_kbhit()) snake.change_dir(_getch());
		update_map();
		if (!running) break;
		printMap();
		game_speed_increase();
		Sleep(sleep_tick);
	}

}

//���� ���� �� �絵�� ���� ���� �Լ�
int play_again() {
	system("cls");
	for (int i = 0; i < 5; i++) cout << '\n';
	cout << "\t\t\tGAME OVER!!\n";
	cout << "\t\t\tYour Score is " << snake.score() << ". Press Y to play again.";
	char cmd = _getch();
	if (cmd == 'y' || cmd == 'Y') return 1;
	else return 0;
}

//�ʿ��� ���̸� �����ϰ� ��� �� �������� �ʱ�ȭ�ϴ� �Լ�
void clearMap() {
	for (int i = 1; i < height - 1; ++i) {
		for (int j = 1; j < width - 1; ++j) {
			if (map[i][j] != 'a' && map[i][j] != 'A')
				map[i][j] = ' ';
		}
	}
}

//������ AI ����Ͽ� �ۼ��� �Լ�.
//������ : system("cls")�� ��ü�� ����� �ٽ� ����ϴ� ������ ȭ�� ������Ʈ�� ȭ���� �����Ÿ��� ��ó�� ����.
//�ذ�å : ANSI �̽������� ������ ���. "\x1b[H"�� Ŀ���� 1�� 1�ķ� �ű�� �̽������� ������.
void moveCursorHome() {
	std::cout << "\x1b[H";
}