import sqlite3


#변수 선언, DB연결
con, cur = None, None
ID, NAME, ENG, C, PY, SUM, AVG = "","",0,0,0,0,0
row = None

con = sqlite3.connect("myDB.db")
cur = con.cursor()

#main
def main():         #테이블 중복방지 생성, 메뉴 실행
    cur.execute("CREATE TABLE IF NOT EXISTS students (id TEXT, name TEXT, eng INTEGER, c INTEGER, py INTEGER, sums INTEGER, avgs FLOAT, grade TEXT, rank INTEGER)")
    con.commit()
    while True:
        if menu() == 0:
            break
    con.commit()
    con.close()

def menu():     #메뉴 선택해서 해당하는 명령을 실행하는 함수
    result = 1
    print("--------------------------------------------------------------------")
    cmd = int(input("\n 1. 추가\n 2. 삭제\n 3. 탐색(학번->이름)\n 4. 탐색(이름->학번)\n 5. 80점 이상 카운트 출력\n 6. 출력\n 0. 프로그램 종료\n"))
    if cmd == 1: insert_std()
    elif cmd == 2: delete_std()
    elif cmd == 3: id_to_name()
    elif cmd == 4: name_to_id()
    elif cmd == 5: count_over_80()
    elif cmd == 6: print_table()
    elif cmd == 0: result = 0 #프로그램 종료
    else: print("\n잘못된 명령어입니다. 다시 입력해주세요.\n")
    return result

def input_info():       #학생의 기본 정보(학번, 이름, 3과목 성적)을 입력받는 함수
    
    D1 = input("학번 입력>>")
    D2 = input("이름 입력>>")
    D3 = int(input("영어 성적 입력>>"))
    D4 = int(input("C언어 성적 입력>>"))
    D5 = int(input("파이썬 성적 입력>>"))
    return D1, D2, D3, D4, D5

def sum_and_avg_calc(eng, c, py):   #총점과 평균을 계산해서 반환하는 함수
    DSUM = eng + c + py
    DAVG = DSUM / 3
    return DSUM, DAVG

def grade_calc(DAVG):    #학점을 계산해서 반환하는 함수
    if DAVG >= 90: return "A"
    elif DAVG >= 80: return "B"
    elif DAVG >= 70: return "C"
    elif DAVG >= 60: return "D"
    else: return "F"

def print_table():  #테이블 전체를 출력하는 함수
    print("학번            이름     영어  C언어  파이썬  총점  평균     학점  등수")
    print("--------------------------------------------------------------------")
    cur.execute("SELECT * FROM students")
    while True:
        row = cur.fetchone()
        if row == None:
            break
        DID = row[0]    #string
        DNAME = row[1]  #string
        DENG = row[2]   #int
        DC = row[3]     #int
        DPY = row[4]    #int
        DSUM = row[5]   #int
        DAVG = row[6]   #float
        DGRADE = row[7] #string
        DRANK = row[8]
        print("%-15s %-5s %-5d %-6d %-6d %-5d %-8.2f %-4s %-4d" % (
            DID, DNAME, DENG, DC, DPY, DSUM, DAVG, DGRADE, DRANK))

def insert_std():   #학생을 테이블에 삽입하는 함수. 이후 sort/rank
    DID, DNAME, DENG, DC, DPY = input_info()
    DSUM, DAVG = sum_and_avg_calc(DENG, DC, DPY)
    DGRADE = grade_calc(DAVG)
    sql = "INSERT INTO students (id, name, eng, c, py, sums, avgs, grade, rank) VALUES(?,?,?,?,?,?,?,?,?)"     #학번 이름 영어 C Py 합 평균 학점 등수
    cur.execute(sql, (
        DID, DNAME, DENG, DC, DPY, DSUM, DAVG, DGRADE, 0))
    con.commit()
    sort_and_rank_std()
    
def delete_std():   #학생을 테이블에서 삭제하는 함수. 이후 sort/rank
    DID = input("삭제할 학생의 학번 입력>>").strip()
    sql = "DELETE FROM students WHERE id = ?"
    cur.execute(sql, (DID,))
    con.commit()
    sort_and_rank_std()
    
def name_to_id():   #학번을 입력받아 탐색 후 이름 출력(이름과 학번 모두 유일성을 만족함을 가정)
    DNAME = input("탐색할 학생의 이름 입력>>")
    sql = "SELECT id FROM students WHERE name = ?"
    cur.execute(sql, (DNAME,))
    result = cur.fetchone()
    if result:
        print(f"{DNAME}님의 학번: {result[0]}")
    else:
        print(f"{DNAME}님은 존재하지 않습니다.")
    
def id_to_name():   #이름을 입력받아 탐색 후 학번 출력
    DID = input("탐색할 학생의 학번 입력>>").strip()
    sql = "SELECT name FROM students WHERE id = ?"
    cur.execute(sql, (DID,))
    result = cur.fetchone()
    if result:
        print(f"{DID}님의 이름:{result[0]}")
    else:
        print(f"{DID}님은 존재하지 않습니다.")
        
def sort_and_rank_std():    #정렬 및 등수 구하기
    #총점 기준 내림차순
    cur.execute("SELECT * FROM students ORDER BY sums DESC")
    rows = cur.fetchall()
    #데이터 삭제 후 다시 넣기
    cur.execute("DELETE FROM students")
    for row in rows:
        cur.execute("INSERT INTO students VALUES (?,?,?,?,?,?,?,?,?)", row)
    con.commit()
    #랭크 계산
    cur.execute("""
    WITH ranked AS (
      SELECT id, RANK() OVER (ORDER BY sums DESC) AS rnk
      FROM students
    )
    UPDATE students
    SET rank = (
      SELECT rnk FROM ranked WHERE students.id = ranked.id
    )
    """)
    con.commit()

def count_over_80():    #80점 이상 학생 수 출력
    cur.execute("SELECT COUNT(*) FROM students WHERE avgs >= 80")
    cnt = cur.fetchone()[0]
    print(f"평균 80점 이상 학생 수: {cnt}명")


#아래는 메인 함수

main()