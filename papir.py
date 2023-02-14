class Iskolapapír:
    def __repr__(self):
        if iskola1_papir > iskola2_papir:
            return f"A(z) {iskola1} iskola több papírt gyűjtött össze, mint a(z) {iskola2}. Ennyivel: {iskola1_papir-iskola2_papir}"
        elif iskola2_papir > iskola1_papir:
            return f"A(z) {iskola2} iskola több papírt gyűjtött össze, mint a(z) {iskola1}. Ennyivel: {iskola2_papir-iskola1_papir}"
        else:
            return f"A két iskola azonos számú papírt gyűjtött össze."
iskola1 = input('Egyik Iskola neve: ')
iskola1_papir = int(input('Hány kg papírt gyűjtött? '))
iskola2 = input('Másik Iskola neve: ')
iskola2_papir = int(input('Hány kg papírt gyűjtött? '))
t = Iskolapapír()
print(f'{t}')
