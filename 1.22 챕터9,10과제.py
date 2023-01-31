#문제 1-1
def main():
    ds = (1, 2, 3)
    ds1 = list(ds)
    print(ds1)
main()

def main():
    text = "hello"
    text1 = list(text)
    print(text1)
main()


#문제 2-1
def main():
    for i in range(9, 0, -1):
        print(7 * i )
main()

#문제 2-2
def main():
    for i in tuple(range(1,101)):
        x = (i)
        print(x, end = " ")
    for o in tuple(range(101,1,-1)):
        y = o - 1
        print(y, end = " ")
main()


#챕터 10

#문제 1-1
def main():
    for i in range(3):
        i+= 1
        print(i)
    for i in range(3):
        i+=2
        print(i)
    for i in range(3):
        i+=3
        print(i)
main()

#문제 2-1  
st = [1,2,3,4,5]
def add1(st):
    for i in st:
        i+= 1
        print(i, end = " " )
        
add1(st)



