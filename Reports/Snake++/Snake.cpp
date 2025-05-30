#include "Snake.h"

pair <int, int> direction[4] = { {-1,0},{0,-1},{1,0},{0,1} };

Snake::Snake(int width, int height) {   //생성자
    length = 1;
    dir = direction[1];
    body.push_back({ width / 2, height / 2 ,'@' });
}

void Snake::change_dir(char key) {      //입력받은 키값에 따라 방향 전환
    if (key == 'w' && dir != direction[2])
        dir = direction[0];
    else if (key == 'a' && dir != direction[3])
        dir = direction[1];
    else if (key == 's' && dir != direction[0])
        dir = direction[2];
    else if (key == 'd' && dir != direction[1])
        dir = direction[3];
}

void Snake::append(int count) {         //먹이or슈퍼먹이 획득 시 길이 증가
    for (int i = 0; i < count; i++) {
        body.push_back({ body.back().x,body.back().y, 'O' });
        length++;
    }
}

void Snake::move() {                    //움직이기
    for (int i = length - 1; i > 0; i--) {
        body[i].x = body[i - 1].x;
        body[i].y = body[i - 1].y;
    }
    body[0].y += dir.first;
    body[0].x += dir.second;
}
int Snake::score() {                    //길이(==점수) 리턴
    return length;
}

pair<int, int> Snake::head() {          //머리의 좌표만 리턴
    return { body[0].y, body[0].x };
}

vector<part> Snake::bodyvector() {    //벡터 통째로 리턴
    return body;
}
