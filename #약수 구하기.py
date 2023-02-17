def main():
    try:
        n = int(input("입력:"))
        a = []
        for i in range(1,n+1):
            if n % i == 0:
                a.append(i)
                b = (",".join(str(x) for x in a))
        print("입력한 수의 약수는{}".format(b))
        print("약수의 개수는{}개 입니다.".format(len(a)))
    except ValueError:
        print("문자열 입력했다")
    except TypeError:
        print("ㅇ")
    except IndexError:
        print("이건가?")
main()