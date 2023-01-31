def main():
    num = int(input("숫자를 입력하세요.> "))
    for i in range(1, num+1):
        i = str(i)
        if i.count("2"):
            print("#", end = " ")
        elif i.count("4"):
            print("#", end = " ")
        elif i.count("8"):
            print("#", end = " ")
        else:
            print(i, end = " ")
main()



def main():
    num = int(input("숫자를 입력하세요.> "))
    for i in range(1,num+1):
        if i % 2 == 0 or i % 4 == 0 or i % 8 == 0:
            print("#", end = " ")
        else:
            print(i, end = " ")
main()






def main():
    num = int(input("숫자를 입력하세요.> "))
    for i in range(1,num+1):
        if i % 20 == 0:
            print(i)
        elif i % 10 == 2 or i % 10 == 4 or i % 10 == 8:
            print("#", end = " ")
        else:
            print(i, end = " ")
main()


def main():
    num = int(input("숫자를 입력하세요.> "))
    for i in range(1, num+1):
        i = str(i)
        if i.count("2") or i.count("4")or i.count("8"):
            print("#", end = " ")
        elif i.count("30"):
            print(i)
        else:
            print(i, end = " ")
main()

def main():
    print("-" * 20)
    print("<나의 계산기>")
    print("-" * 20)
    print("1. 입\t력", "\t", "2. 덧\t셈", "\t", "3. 뺄\t셈")
    print("4. 곱\t셈", "\t", "5.나눗셈", "\t", "6. 종\t료")
    choice = int(input("메뉴 선택(1~6)"))
    a,b = input("숫자 2개 입력(예: 1,7)").split(",")
    a = int(a)
    b = int(b)
    if choice == 1:
        print(a,b)
    elif choice == 2:
        print(a,"+",b,"=",a+b)
    elif choice == 3:
        print(a-b)
    elif choice == 4:
        print(a*b)
    elif choice == 5:
        print(a / b)
    elif choice == 6:
        print("end")
main()



def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("사칙연산을 선택 하세요.")
print("1.더하기")
print("2.빼기")
print("3.곱하기")
print("4.나누기")

choice = input("선택 하세요(1/2/3/4):")

num1 = int(input("첫번째 숫자 : "))
num2 = int(input("두번째 숫자 : "))

if choice == '1':
    print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
    print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
    print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
    print(num1,"/",num2,"=", divide(num1,num2))
else:
    print("잘못된 선택")






#https://m.blog.naver.com/dhsjid/221220034644























