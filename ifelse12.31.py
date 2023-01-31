#if 조건문은 컴파일러가 인식할때 각자(if else elif) 각자 인식하는게 아니라 하나의 세트(묶음)로 인식한다.

'''def main():
    num1 = 10
    num2 = 20

    if(num1 > num2):  # 혼자사용가능 Ture 실행 Flase 실행하지 않음
        print("num1이 num2보다 큽니다.")
    else:  #혼자 사용 불가 If 와 같이 써야함 #문법
        print("num2가 num1보다 큽니다.")
        
main()'''

''' def main():
    num = 17

    if(num < 0):
        print("음수입니다.")
    elif (num == 0): #else if 조건이 여러가지 일떄 Ture 실행 False 실행X
        print("0입니다.")
    else:
        print("양수입니다.")

main() '''

''' def main():
    age = 22

    if(age > 18):
        print("운전면허 취득 불가능")
    elif(18 < age):  #->수정: elif(18<= age and age < 20) = 18<= age < 20 같은 의미 
        print("오토바이 면허 취득 가능")
    elif(20 < age):
        print("운전면허 취득 가능")

main() '''

''' def fac(num):   
    if(num == 1):
        return 1
    else:
        return num * fac(num - 1) '''

'''def main():
    number = int(input("팩토리얼을 구할 수를 입력 : "))
    print(number, "의 팩토리얼: ", fac(number))
main()'''

''' def car(n1, n2):
    if n2 == 1:
        return n1
    else:
        print("모르겠소")
print(car(2,3)) '''

#6!을 구해보시오
# 반복문
def main(a):
    ouput = 1
    for i in range(1, a+1):
        ouput *= i
    return ouput
print(main(6))
#재귀 함수
def main(b):
    if b == 0 :
        return 1
    else:
        return b * main(b - 1)
print(main(2))

def main():
    for i in range(3):
        print("---------------------")
        for j in range(3):
            print("[", i, ",", j, "]", end = " ")
        print("")
main()



def main():
    for i in range(2,10):
        print(i)
        for j in range(1,10):
            print( i, "X", j, "=", i * j)
        print("")
main()


def main():
i = "*"
    for  i in range(15):
        print(14, I ,-1)
main()



def main():
    output = ""
    for i in range(15):
        for j in range(14,i,-1):
            output += ""
        for k in range(0,2 * i -1):
            output += '*'
        output += "\n"
            
            
main()

