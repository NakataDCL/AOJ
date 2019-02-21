# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0007&lang=jp

debt = 100000

weeks = int(input())
for i in range(weeks):
    debt = int(debt * 1.05)
    frac = debt % 1000
    if frac != 0:
        debt = debt - frac + 1000
print(debt)
