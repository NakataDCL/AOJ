# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0004&lang=jp

while True:
    try:
        input_set = list(map(float, input().split()))
        a, b, c, d, e, f = input_set
        y = (d*c - a*f)/(d*b - a*e)
        x = (e*c - b*f)/(e*a - b*d)
        print('%.3f %.3f' % (x, y))
    except EOFError:
        break
