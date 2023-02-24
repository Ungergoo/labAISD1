f = open('labtext1.txt', 'r')
massiv = f.read().split()
massiv2 = []
k = int(input())
for i in range(len(massiv)):
    if len(massiv[i]) == k:
        massiv2.append(int(massiv[i]))
abc = ('ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять')
minnum = (min(massiv2))
print(len(massiv2))
for j in str(minnum):
    for k in range(10):
        if j == str(k):
            print(abc[k])
        
