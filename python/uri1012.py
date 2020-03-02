A, B, C = input().split(' ')
A = float(A)
B = float(B)
C = float(C)
trian = (A * C)/2
circ = 3.14159 * C**2
trap = ((A + B) *C)/2
qua = B**2
ret = A * B
print('TRIANGULO: {:.3f}'.format(trian))
print('CIRCULO: {:.3f}'.format(circ))
print('TRAPEZIO: {:.3f}'.format(trap))
print('QUADRADO: {:.3f}'.format(qua))
print('RETANGULO: {:.3f}'.format(ret))
