# isupper, islower, join 함수 사용
# 'Merry Christmas HaPPy New YEaR'
# mERRY CHRISTMAS hAppY nEW yeAr 출력되게 만드시오
'''def main():
    num = ["Merry", "Christmas", "HaPPy", "New", "YEaR"]
    i = []
    print(type(num))
    if num[0].isupper == True and num[1].isupper == True:
        print("거짓")
    else:
        i.append("mERRy")
        i.append("cHRISTMAS")
        print(i)
main()'''

def main():
    num = ["M","e","r","r","y"," ","C","h","r","i","s","t","m","a","s"," ","H","a","P","P","y"," ","N","e","w"," ","Y","E","a","R"]
    print("".join(num))
    for i in num:
        num1 = []
        if i.isupper() == True:
            num1.append(i.lower())
        elif i.islower() == True:
            num1.append(i.upper())
        else:
            num1.append(" ")
        print("".join(num1), end = "")
main()