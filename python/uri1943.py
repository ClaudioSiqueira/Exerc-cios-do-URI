num = int(input())
top = 0
if num == 1:
    top = 1
elif num == 3 or num == 2:
    top = 3
elif 4 <= num <= 5:
    top = 5
elif 6 <= num <= 10:
    top = 10
elif 11 <= num <= 25:
    top = 25
elif 26 <= num <= 50:
    top = 50
elif 51 <= num <= 100:
    top = 100
print('Top %i' % top)
