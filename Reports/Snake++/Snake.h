#ifndef SNAKE_H
#define SNAKE_H

#include <vector>
#include <utility>
using namespace std;
struct part{
    int x;
    int y;
    char type;
};
extern pair<int, int> direction[4];

class Snake {
    int length;
    vector<part> body;
    pair<int, int> dir;

public:
    Snake(int width, int height);
    void change_dir(char key);
    void append(int count);
    void move();
    pair<int,int> tail();
    int score();
    pair<int, int> head();
    vector<part> bodyvector();
};

#endif
