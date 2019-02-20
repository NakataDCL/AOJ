# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0003&lang=jp

input_num = int(input())

for i in range(input_num):
    sides = list(map(int, input().split()))
    sides.sort()
    a, b, c = sides
    if a*a + b*b == c*c:
        print('YES')
    else:
        print('NO')
