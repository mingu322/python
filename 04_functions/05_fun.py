# 실행하면 콘솔에서 1또는 2를 입력받고 1은 세로형구구단 2는 가로형 구구단을 각각 출력한다.
# 구구단은 각각 함수로 정의하도록 한다.

def fun1():
    # 새로형
    for i in range(2,10):
        dan = "단"
        print(str(i)+str(dan))
        for j in range(1, 10):
            print(str(i)+ "*" +str(j)+ "=" +str(i*j))

def fun2():
    # 가로형
    dan = "단"
    for i in range(2,10):
        print(str(i)+str(dan))

        for j in range(1, 10):
            print(str(i)+ "*" +str(j)+ "=" +str(i*j), end="  ")
        print()  


run = True
while run:
    sel = int (input("선택: "))
    if sel == 1:
        # print("1번 선택")
        fun1()
    elif sel == 2:
        # print("2번 선택")
        fun2()
    elif sel == 3:
        print("종료")
        run = False

print("종료되었습니다.")