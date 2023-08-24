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