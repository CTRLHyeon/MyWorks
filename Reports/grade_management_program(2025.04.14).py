# -*- coding: utf-8 -*-
#######################
#프로그램명: Grade_Management
#작성자: 소프트웨어학부/조정현
#작성일: 2025.04.14
#프로그램 설명: 학생들의 성적을 입력받고 관리(정렬, 탐색, 삽입, 삭제 등)하는 프로그램
######################
class student:
    def __init__(self, studentID, name, eng, clang, py, sums, avgs):
        self.studentID = studentID
        self.name = name
        self.eng = eng
        self.clang= clang
        self.py = py
        self.sums = sums
        self.avgs = avgs
#made class to sort
        
studentList = []
students = int(5)    #initial number of students, can be modified through insert()/delete()
def inputs():       #receiving input
    for i in range(0,students, 1):
        tempID = input("학번: ")
        tempName = input("이름: ")
        tempEng = int(input("영어: "))
        tempC = int(input("C언어: "))
        tempPy = int(input("파이썬: "))
        studentList.append(student(tempID,tempName,tempEng, tempC, tempPy, 0, 0))
        #sum and avg is appended with value 0, 0 (will be calculated soon)
        
def calc():    #calc(): calculate sum and avg
    global studentList
    for i in range(0,students,1):
        studentList[i].sums = studentList[i].eng + studentList[i].clang + studentList[i].py
        studentList[i].avgs = studentList[i].sums / 3
        
    
def ranks(a):       #ranks(): calculate ranks, parameter: sum object of studentList
    rank=[]
    for i in range(0,students,1):
        rank.append(int(1))
        
        temp =int(a[i].sums)
        for j in range(0,students,1):
            if (a[j].sums>temp):
                rank[i]+=1
    return rank

def grades(a):      #grades(): calculate grade, parameter: sum object of studentList
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
    print("학번\t\t이름\t\t영어\t\tC-언어\t\t파이썬\t\t총점\t\t평균\t\t학점\t\t등수")
    studentRank = ranks(studentList)
    studentGrade = grades(studentList)
    
    for i in range(0,students,1):
        print(studentList[i].studentID, "\t",studentList[i].name, "\t\t", studentList[i].eng, "\t\t", studentList[i].clang, "\t\t", studentList[i].py, "\t\t", studentList[i].sums, "\t\t", studentList[i].avgs, "\t\t", studentGrade[i], "\t\t", studentRank[i])
        

def insert():   #insert(): insert to studentList and +1 to student
    global students
    print("삽입할 학생의 정보 입력(학번, 이름, 영어점수, C-언어 점수, 파이썬 점수를 공백으로 구분하여 입력)")
    tempID, tempName, tempEng, tempC, tempPy = input().split()  #input datas temporarily
    a=int(input("몇번째에 삽입?: "))
    studentList.insert(a, student(tempID, tempName, int(tempEng), int(tempC), int(tempPy), 0, 0))
    students += 1
    calc()   #execute calc() to calculate inserted index's sum and avg
    print('삽입 완료. 출력 명령을 통해 결과 확인 가능')
                
def delete():   #delete(): find stuendID in studentList, and remove corresponding index
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
            
def sorting():  #sorting(): sort(ascending) using lambda func
    global studentList
    studentList = sorted (studentList, key = lambda x: x.sums)
    #sort(ascending) by students' sum score
    print("정렬 완료. 출력 명령을 통해 결과 확인 가능")
    
def over80():
    cnt = 0
    for i in studentList:
        if (i.avgs >= 80 ):
            cnt +=  1
    print("평균 80점 이상 학생의 수: ", cnt)
    
def menu():
    
    while (1):
        print("\n\n명력 선택\n1. 삽입\n2. 삭제\n3. 탐색\n4. 정렬\n5. 출력\n6. 80점 이상 학생수 출력\n0. 종료")
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
        elif (cmd == 6):
            over80()
        else:
            break
def main():
    inputs()
    calc()
    menu()
    
    #============================================================
    #main func below

main()