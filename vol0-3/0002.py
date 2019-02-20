# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0002&lang=jp

while True:
    try:
        a, b = map(int, input().split())
        print(len(str(a+b)))
    except:
        exit(0)
