cont = int(input())
quebrou = 0
for i in range(cont):
    l, c = map(int, input().split(' '))
    if c < l:
        quebrou += c
print(quebrou)
