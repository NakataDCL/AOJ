# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0009&lang=jp

MAX = 1000000

# 素数の表
prime_map = [True] * MAX
prime_map[0] = False
prime_map[1] = False

# n以下の素数の表
prime_num_map = [0] * MAX

for i in range(2, MAX):
    if prime_map[i]:
        prime_num_map[i] = prime_num_map[i-1] + 1
        index = 2
        n = i*index
        while n < MAX:
            prime_map[n] = False
            index += 1
            n = i*index
    else:
        prime_num_map[i] = prime_num_map[i-1]

while True:
    try:
        n = int(input())
        print(prime_num_map[n])
    except:
        exit(0)
