# 중첩 for문을 이용하여 구구단을 세로형, 가로형으로 각각 만들어봅시다.
# 새로형
for i in range(2,10):
    dan = "단"
    print(str(i)+str(dan))
    for j in range(1, 10):
       print(str(i)+ "*" +str(j)+ "=" +str(i*j))

print()

# 가로형
dan = "단"
for i in range(2,10):
    print(str(i)+str(dan))

    for j in range(1, 10):
        print(str(i)+ "*" +str(j)+ "=" +str(i*j), end="  ")
    print()           

    