N = int(input())
hora = N//3600
minu = (N % 3600)// 60
seg = (N % 3600)% 60
print('{}:{}:{}'.format(hora, minu, seg))
