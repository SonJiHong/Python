#짝수 구구단

def main():
    for i in range(2,10,2):
        print(i,"dan")
        for i in range(i):
            i+= 1
            print(i, "X", i, "=", i * i)
main()


#시분초 구하   1시간은 60 분 3600
def main():
    
    s = int(input("초"))
    hours = s // 3600
    s = s- hours * 3600
    mu = s // 60
    ss = s - mu * 60
    print(hours, "시", mu , "분", ss, "초")
    
main()

