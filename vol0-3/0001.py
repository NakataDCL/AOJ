# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0001&lang=jp

# 入力を格納
input_arr = []
for i in range(10):
    input_arr.append(int(input()))

input_arr.sort(reverse=True)

for i in range(3):
    print(input_arr[i])
