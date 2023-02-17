#예외 처리
def main():
    print("안녕하세요")
    while True:
        age = (input("나이입력"))
        if age == age.int:
            print("나이는",age)
            break
        else:
            print("다시입력")
main()