#include <iostream>
#include <conio.h>
#include <vector>
#include <Windows.h>
#include <time.h>
#include "Snake.h"
#define DEFAULT_SPEED 200
using namespace std;

//------------전역변수-----------------
int width = 30;
int height = 20;
int size = width * height;
double sleep_tick = DEFAULT_SPEED;
int running = 0;
int speed_up = 5;
vector<vector<char>> map(height, vector<char>(width, ' '));
//	#: 벽, @: 스네이크 머리. O: 스네이크 몸, A: 슈퍼 먹이, a: 일반 먹이
Snake snake(width, height);
//-----------------------------------

//------------함수선언----------------
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

//------------함수정의----------------

//게임 초기 실행 or 다시 실행시 맵과 스네이크를 초기화
void init() {
	//map 초기화
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

	//snake 초기화
	Snake temp(width, height);
	snake = temp;
	food_gen();
}

//맵의 상태를 업데이트 하는 함수
//스네이크를 움직이게하고 충돌을 감지. 이후 스네이크의 위치를 옮김.
void update_map() {
	clearMap();
	snake.move();
	for (auto i : snake.bodyvector())
		if (i.type != '@') map[i.y][i.x] = i.type;
	checkCollision();
	for (auto i : snake.bodyvector()) map[i.y][i.x] = i.type;
}

//맵 출력, 점수 출력 함수
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

//메인화면 출력
void printMain() {
	system("cls");
	for (int i = 0; i < 5; i++) cout << '\n';
	cout << "\t\t\tSnake Game. Press any key to start.";
	_getch();
	system("cls");
}

//스네이크의 충돌 감지
void checkCollision() {
	char current = map[snake.head().first][snake.head().second];
	if (current != ' ' && current != '@') {			//벽도 머리도 아닐때(어딘가에 충돌)
		if (current == 'a') {
			snake.append(1);		//일반먹이: 길이 +1
			food_gen();
		}
		else if (current == 'A') {
			snake.append(3);	//슈퍼먹이: 길이 +3
			food_gen();
		}
		else running = 0;
	}
}

// 랜덤으로 먹이 생성
void food_gen() {
	int x = rand() % width;
	int y = rand() % height;
	while (map[y][x] != ' ') {
		x = rand() % width;
		y = rand() % height;
	}
	int count = rand() % 100 + 1;
	//25% 확률로 슈퍼먹이, 75% 확률로 일반 먹이
	if (count > 75) map[y][x] = 'A';
	else map[y][x] = 'a';
}

//사이즈에 따라 게임 속도 증가
void game_speed_increase() {
	if (snake.score() - speed_up > 0) {
		sleep_tick *= 0.9;
		speed_up += 5;
	}
}

//게임의 전반적인 실행을 담당하는 함수
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

//게임 오버 후 재도전 여부 묻는 함수
int play_again() {
	system("cls");
	for (int i = 0; i < 5; i++) cout << '\n';
	cout << "\t\t\tGAME OVER!!\n";
	cout << "\t\t\tYour Score is " << snake.score() << ". Press Y to play again.";
	char cmd = _getch();
	if (cmd == 'y' || cmd == 'Y') return 1;
	else return 0;
}

//맵에서 먹이를 제외하고 모두 빈 공간으로 초기화하는 함수
void clearMap() {
	for (int i = 1; i < height - 1; ++i) {
		for (int j = 1; j < width - 1; ++j) {
			if (map[i][j] != 'a' && map[i][j] != 'A')
				map[i][j] = ' ';
		}
	}
}

//생성형 AI 사용하여 작성한 함수.
//문제점 : system("cls")로 전체를 지우고 다시 출력하는 식으로 화면 업데이트시 화면이 깜빡거리는 것처럼 보임.
//해결책 : ANSI 이스케이프 시퀀스 사용. "\x1b[H"은 커서를 1행 1렬로 옮기는 이스케이프 시퀀스.
void moveCursorHome() {
	std::cout << "\x1b[H";
}