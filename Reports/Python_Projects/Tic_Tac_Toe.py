# -*- coding: utf-8 -*-
def check():    #빙고가 맞춰졌는지 확인하는 함수. 플레이어가 이길 시 0, 컴퓨터가
                #이길 시 1, 아직 판정나지 않으면 2를 return
    #플레이어가 대각선으로 이길 경우
    if (board[0][0] == board[1][1] == board[2][2] == 'X'):
        return 0
    elif (board[0][0] == board[1][1] == board[2][2] == 'O'):
        return 0
    #컴퓨터가 대각선으로 이길 경우
    if (board[0][0] == board[1][1] == board[2][2] == 'O'):
        return 1
    elif (board[0][2] == board[1][1] == board[2][0] == 'X'):
        return 1
    #가로 행 조사
    for i in range(3):
        Ocount = 0
        Xcount = 0
        for j in range(3):
            if (board[i][j] == 'O'):
                Ocount += 1
            elif (board[i][j]== 'X'):
                Xcount += 1
            if (Ocount == 3):
                return 1
            elif (Xcount == 3):
                return 0
    #세로 열 조사
        for i in range(3):
            Ocount = 0
            Xcount = 0
            for j in range(3):
                if (board[j][i] == 'O'):
                    Ocount += 1
                elif (board[j][i]== 'X'):
                    Xcount += 1
                if (Ocount == 3):
                    return 1
                elif (Xcount == 3):
                    return 0
        #모든 조건을 만족하지 않는 경우 2(아무도 이기지 않음) return
        return 2
            

board= [[' ' for x in range (3)] for y in range(3)]

while True:
    for r in range(3):
        print(" " + board[r][0] + "| " + board[r][1] + "| "+ board[r][2])
        if (r != 2):
            print("---|---|---")
            #출력
    
    x = int(input("다음 수의 y좌표 입력: "))
    y = int(input("다음 수의 x좌표 입력: "))
    if (board[x][y] != ' '):
        print("잘못된 위치입니다.")
        continue
    else:
        board[x][y]='X'
    #플레이어의 차례가 끝난 후 승리 여부 조사
    result = check()
    if (result == 0):
        print("\n플레이어가 승리했습니다!")
        break
    elif (result == 1):
        print("\n컴퓨터가 승리했습니다!")
        break
    else:
        print('\n')
    
    done = False    #이중 반복문 탈출을 위한 변수
    for i in range(3):
        for j in range(3):
            if (board[i][j]==' ' and not done):
                board[i][j]='O'
                done = True
                break
    #컴퓨터의 차례가 끝난 후 승리 여부 조사
    result = check()
    if (result == 0):
        print("\n플레이어가 승리했습니다!")
        break
    elif (result == 1):
        print("\n컴퓨터가 승리했습니다!")
        break
    else:
        print('\n')
