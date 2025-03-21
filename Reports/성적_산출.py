# -*- coding: utf-8 -*-
studentID=[]    #학번
name=[]         #이름
eng=[]          #영어
clang=[]        #C
py=[]           #pyhton

def inputs():       #입력받는 함수
    for i in range(0,5,1):
        studentID.append(input("학번: "))
        name.append(input("이름: "))
        eng.append(int(input("영어: ")))
        clang.append(int(input("C-언어: ")))
        py.append(int(input("파이썬: ")))
        
def SumAvg(a,b,c):  #합과 평균 출력 함수, 매개변수: 영어, C언어, 파이썬 리스트
    sums=[]
    avgs=[]
    for i in range(0,5,1):
        sums.append(a[i]+b[i]+c[i])
        avgs.append(sums[i]/3)
    return sums, avgs
    
def ranks(a):       #등수 계산, 매개변수: 총점 리스트
    rank=[1,1,1,1,1]
    for i in range(0,5,1):
        temp =int(a[i])
        for j in range(0,5,1):
            if (a[j]>temp):
                rank[i]+=1
    return rank

def grade(a):       #학점 계산, 매개변수: 총점 리스트
    grades=[0,0,0,0,0] #초기화
    for i in range(0,5,1):
        if (a[i]>=285):
            grades[i]="A+"
        elif (a[i]>=270):
            grades[i]="A0"
        elif(a[i]>=255):
            grades[i]="B+"
        elif(a[i]>=240):
            grades[i]="B0"
        elif(a[i]>=225):
            grades[i]="C+"
        elif(a[i]>=210):
            grades[i]="C0"
        else:
            grades[i]="F"
    return grades

def prints():
    print("              성적관리프로그램")
    print("=============================================================================")
    print("학번          이름      영어   C-언어   파이썬   총점   평균   학점   등수")
    for i in range(0,5,1):
        Sum, Avg = SumAvg(eng,clang,py)
        print(studentID[i],"  ",name[i],"  ",eng[i],"  ",clang[i],"  ",py[i],"  ",Sum[i],"  ",Avg[i],"  ",grade(Sum)[i],"  ",ranks(Sum)[i])
        
def main():
    inputs()
    prints()
    
    #============================================================
    #밑에가 메인 함수

main()
