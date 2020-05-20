a, b, c = map(int, input().split())
soma = a + b + c
if soma > 24:
    print(soma - 24)
elif soma < 0:
    print(soma + 24)
else:
    print(soma)
