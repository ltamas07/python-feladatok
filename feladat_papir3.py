class Iskolapapír:
    def __repr__(self):
        if papir > 1000:
            return f"Szorgalmas Iskola, mert {papir} kg papírt gyűjtöttek össze."
        else:
            return f"Kevésbé szorgalmas Iskola, mert csak {papir} kg papírt gyűjtöttek össze."
iskolanév, város, papir = None, None, None
while iskolanév != "" and város != "" and papir != 0:
    iskolanév = input('Iskola neve: ')
    város = input('Iskola városa: ')
    papir = int(input('Gyűjtött papír mennyisége: '))
    t = Iskolapapír()
    print(f'Az {iskolanév} iskola ami {város} városban található, egy {t}')
else:
    quit()