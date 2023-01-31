#문제 1-1, 1-2 ,1-3
''' def main():
    dc = {'새우깡': 700, '콘치즈': 850, '꼬깔콘': 750}
    dc['홈런볼'] = 900
    print(dc)
    for i in dc:
        dc[i] += 100
    print(dc)
    del dc['콘치즈']
    print(dc)
    dc['치즈콘'] = 950
    print(dc)
main() '''

# in not in 연산자 사용
def main():
    dc = {'새우깡': 700, '콘치즈': 850, '꼬깔콘': 750}
    dc['홈런볼'] = 900
    print(dc)
    for i in dc:
        dc[i] += 100
    print(dc)
    print('여')
    if '콘치즈' in dc:
        del dc['콘치즈']
        print(dc)
    if '콘치즈' not in dc:
        dc['치즈콘']= 950
        print(dc)
main()
