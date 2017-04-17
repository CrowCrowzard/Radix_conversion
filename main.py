from cal import *

def main():
    s = input("計算を入力してください:")
    x, c, y = s.split(' ')
    x = conv10(x)
    y = conv10(y)

    cal = 0
    if (c == '+'):
        cal = x + y
    elif (c == '-'):
        cal = x - y
    elif (c == '*'):
        cal = x * y
    elif (c == '/'):
        cal = x / y

    print (conv26(cal))

if __name__ == '__main__':
    main()

