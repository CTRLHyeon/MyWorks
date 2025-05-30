#include "Snake.h"

pair <int, int> direction[4] = { {-1,0},{0,-1},{1,0},{0,1} };

Snake::Snake(int width, int height) {   //������
    length = 1;
    dir = direction[1];
    body.push_back({ width / 2, height / 2 ,'@' });
}

void Snake::change_dir(char key) {      //�Է¹��� Ű���� ���� ���� ��ȯ
    if (key == 'w' && dir != direction[2])
        dir = direction[0];
    else if (key == 'a' && dir != direction[3])
        dir = direction[1];
    else if (key == 's' && dir != direction[0])
        dir = direction[2];
    else if (key == 'd' && dir != direction[1])
        dir = direction[3];
}

void Snake::append(int count) {         //����or���۸��� ȹ�� �� ���� ����
    for (int i = 0; i < count; i++) {
        body.push_back({ body.back().x,body.back().y, 'O' });
        length++;
    }
}

void Snake::move() {                    //�����̱�
    for (int i = length - 1; i > 0; i--) {
        body[i].x = body[i - 1].x;
        body[i].y = body[i - 1].y;
    }
    body[0].y += dir.first;
    body[0].x += dir.second;
}
int Snake::score() {                    //����(==����) ����
    return length;
}

pair<int, int> Snake::head() {          //�Ӹ��� ��ǥ�� ����
    return { body[0].y, body[0].x };
}

vector<part> Snake::bodyvector() {    //���� ��°�� ����
    return body;
}
