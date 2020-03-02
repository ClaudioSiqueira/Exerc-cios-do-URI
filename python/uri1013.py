#Utilizando a fórmula: (Essa resolução foi aceita pelo uri)
#Calcular o maior utilizando a fórmula


#Ler
a,b,c = [int(x) for x in input().split()]


#Calcular o maior 
maiorAB = int( ( (a+b+abs(a-b)) )/2)
maiorAC = int ( ( (a+c+abs(a-c)) )/2)
maiorCB = int( ( (c+b+abs(c-b)) )/2) 


#Imprimir o resultado
if  maiorAB >= maiorAC and maiorAB >= maiorCB:
    print(maiorAB,"eh o maior")
elif maiorAC >= maiorCB:
    print(maiorAC,"eh o maior")
else:
    print(maiorCB,"eh o maior")