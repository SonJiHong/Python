# 챕터6
#문제 1-1
def main():
    st = []
    st.append(1)
    st.append(2)
    st.append(3)
    print(st)
main()

def main():
    st = [1,2,3]
    del st[:3]
    print(st)
main()

#문제 1-2
def list():
    list1 = [1,2,3]
    list1.pop(-1), list1.pop(1), list1.pop(0)
    print(list1)
list()


#문제 1-3 #clear 함수로 대신해 슬라이싱
def main():
    st = [1,2,3,4]
    st[:] = []
    print(st)
main()

#문제 1-4
def main():
    st = []
    for i in range(11):
        print(st)
main()

def main():
    st = []
    for i in range(11):
        st.pop(-1)
        print(i)
main()
print(" ")

''' def main():
    for i in reversed(range(1,11)):
        st = [i]
        print(st)
        st.pop(0)
        print(st)
main() '''

def main():
    for i in range(10 ,0, -1):
        st = [i]
        print(st)
        st.pop(0)
        print(st)
main()

''' def main():
    st = []
    for i in range(11):
        if i < 10:
            i += 1
            st = [i]
            print(st)
        else:
            st.pop()
main() '''
