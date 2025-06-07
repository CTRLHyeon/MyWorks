# -*- coding: utf-8 -*-
class student:
    def __init__(self, studentID, name, eng, clang, py, sums, avgs):
        self.studentID = studentID
        self.name = name
        self.eng = eng
        self.clang= clang
        self.py = py
        self.sums = sums
        self.avgs = avgs
#정렬의 편의를 위해 클래스 생성
        
studentList = []
students = int(5)    #초기 학생의 수: 5명, 이후 삽입/삭제를 통해 변경 가능
def inputs():       #입력받는 함수
    for i in range(0,students, 1):
        tempID = input("학번: ")
        tempName = input("이름: ")
        tempEng = int(input("영어: "))
        tempC = int(input("C언어: "))
        tempPy = int(input("파이썬: "))
        studentList.append(student(tempID,tempName,tempEng, tempC, tempPy, 0, 0))
        #어팬드, 이때 sum과 avg는 나중에 구할 것이므로 0, 0으로 초기화 및 어팬드     
        
def calc():  #총점과 평균 구하는 함수, 매개변수: studentlist (객체 eng, clang, py 사용)
    global studentList
    for i in range(0,students,1):
        studentList[i].sums = studentList[i].eng + studentList[i].clang + studentList[i].py
        studentList[i].avgs = studentList[i].sums / 3
        
    
def ranks(a):       #등수 계산, 매개변수: studentList의 sums객체
    rank=[]
    for i in range(0,students,1):
        rank.append(int(1))
        
        temp =int(a[i].sums)
        for j in range(0,students,1):
            if (a[j].sums>temp):
                rank[i]+=1
    return rank

def grades(a):       #학점 계산, 매개변수: studentList의 sums객체
    grade = []
    for i in range(0,students,1):
        grade.append(0)
        if (a[i].sums>=285):
            grade[i]="A+"
        elif (a[i].sums>=270):
            grade[i]="A0"
        elif(a[i].sums>=255):
            grade[i]="B+"
        elif(a[i].sums>=240):
            grade[i]="B0"
        elif(a[i].sums>=225):
            grade[i]="C+"
        elif(a[i].sums>=210):
            grade[i]="C0"
        else:
            grade[i]="F"
    return grade

def prints():   #출력함수
    print("              성적관리프로그램")
    print("=============================================================================")
    print("학번          이름      영어   C-언어   파이썬   총점   평균   학점   등수")
    studentRank = ranks(studentList)
    studentGrade = grades(studentList)
    
    for i in range(0,students,1):
        print(studentList[i].studentID, " ",studentList[i].name, " ", studentList[i].eng, " ", studentList[i].clang, " ", studentList[i].py, " ", studentList[i].sums, " ", studentList[i].avgs, " ", studentGrade[i], " ", studentRank[i])
        

def insert():   #삽입함수: studentList에 삽입 후 students 변수 1 증가
    global students
    print("삽입할 학생의 정보 입력(학번, 이름, 영어점수, C-언어 점수, 파이썬 점수를 공백으로 구분하여 입력)")
    tempID, tempName, tempEng, tempC, tempPy = input().split()  #정보들 입력받아 임시로 저장
    a=int(input("몇번째에 삽입?: "))
    studentList.insert(a, student(tempID, tempName, int(tempEng), int(tempC), int(tempPy), 0, 0))
    students += 1
    calc()  #평균/출력 함수 한 번 실행하여 새로 삽입한 인덱스의 총점, 평균 객체의 값을 구해줌
    print('삽입 완료. 출력 명령을 통해 결과 확인 가능')
    
def delete():   #삭제함수: studentList에서 학번 찾은 후 해당하는 인덱스 삭제
    global students
    print("삭제할 학생의 학번 입력")
    tempID = input()
    toDelete = 0
    for i in range (0,students,1):
        if (tempID == studentList[i].studentID):
            toDelete = i
    del studentList[toDelete]
    students -= 1
    print("삭제 완료. 출력 명령을 통해 결과 확인 가능")
            
def search():
    a = input("찾으려는 학생의 학번 입력: ")
    for i in studentList:
        if (a == i.studentID):
            print("학생의 학번과 이름: ",a," ", i.name)
            
def sorting():  #정렬함수: 람다함수를 이용하여 오름차순으로 정렬
    global studentList
    studentList = sorted (studentList, key = lambda x: x.sums)
    #학생의 총점을 기준으로 오름차순 정렬
    print("정렬 완료. 출력 명령을 통해 결과 확인 가능")
    
def menu():
    
    while (1):
        print("\n\n명력 선택\n1. 삽입\n2. 삭제\n3. 탐색\n4. 정렬\n5. 출력\n0. 종료")
        cmd = int(input())
        if (cmd == 1):
            insert()
        elif (cmd == 2):
            delete()
        elif (cmd == 3):
            search()
        elif (cmd == 4):
            sorting()
        elif (cmd == 5):
            prints()
        else:
            break
def main():
    inputs()
    calc()
    menu()
    
    #============================================================
    #밑에가 메인 함수

main()