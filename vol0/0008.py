# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0008&lang=jp


def calc(n, x):
    # n個の数(0~9)の和でxが作れるかどうかを判別する
    if n == 1:
        if x <= 9:
            return 1
        else:
            return 0
    else:
        num = 0
        for i in range(10):
            if x-i < 0:
                continue
            num += calc(n-1, x-i)
        return num


while True:
    try:
        print(calc(4, int(input())))
    except:
        exit(0)
