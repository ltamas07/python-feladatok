class Állatfajok:
    def __repr__(self):
        return f'A megadottak közül a legnagyobb állat az {allat}, mert egy példány {legnagyobb} kg'
allatfile = open('allatok.txt','w')
állatok = ['A']
tömegek = [0]
legnagyobb = tömegek[0]
allat = állatok[0]
t = Állatfajok()
for i in range(3):
    állatfaj_neve = input('Add meg az állatfaj megnevezését: ')
    állatok.append(állatfaj_neve)
    állatfaj_súly = int(input('Hány kg egy példány? '))
    tömegek.append(állatfaj_súly)
    if tömegek[i] > legnagyobb:
        legnagyobb = tömegek[i]
        allat = állatok[i]
allatfile.write(f'A megadottak közül a legnagyobb állat az {allat}, mert egy példány {legnagyobb} kg\n')
print(t)
allatfile.close()