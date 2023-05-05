f = open('labtext.txt', 'r')
massiv = f.read().split()
massiv2 = []
k = int(input())
clearm = []
spisok = '0123456789'
for l in massiv:
    stroku = ''
    for o in range(len(l)):
        if (l[o]) in spisok:
            stroku += l[o]
    o+=1
    clearm.append(stroku)
for i in range(len(clearm)):
    if len(clearm[i]) == k:
        massiv2.append(int(clearm[i]))
abc = ('ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять')
if massiv2 == []:
    print("Таких элементов нет")
else:
    minnum = (len(massiv2))
    print(min(massiv2))
    for j in str(minnum):
        for k in range(10):
            if j == str(k):
                print(abc[k])
