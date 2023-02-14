class Diák:
    def __init__(self,név,osztály,szül_év):
        self.név = név
        self.osztály = osztály
        self.szül_év = szül_év
    def Életkor(self,szül_év,életkor):
        self.életkor = életkor
        self.szül_év = szül_év
        életkor = 2023 - self.szül_év
    def Kiir(self):
        return(f'Szia, {self.név} vagyok, a {self.osztály} osztályba járok és {2023-self.szül_év} éves vagyok.')
for _ in range(3):
    név = input('Add meg a Diák nevét: ')
    osztály = input('Add meg a Diák osztályát: ')
    szül_év = int(input('Add meg a Diák születési évét: '))
    li = Diák(név,osztály,szül_év)
    print(f'Szia, {li.név} vagyok, a {li.osztály} osztályba járok és {2023-li.szül_év} éves vagyok.')
    