mae = int(input())
filho1 = int(input())
filho2 = int(input())
filho3 = mae - filho1 - filho2
if filho1 > filho2 and filho1 >filho3:
    maior = filho1
elif filho2 > filho3 and filho2 > filho1:
    maior = filho2
else:
    maior = filho3
print(maior)
