import animales

menu = {
    '1': 'Perro',
    '2': 'Gato',
    '3': 'Camello',
    '4': 'Exit',

}

class Animal:
    perro=0
    gato=0
    camello=0

    animales_lista = {
        1:animales.perro,
        2:animales.gato,
        3:animales.camello

    }
    def __init__(self, perro, gato, camello):
        self.perro = perro
        self.gato = gato
        self.camello = camello

    def mostrar_animal(self, op):
        print(sel.animales_lista[op])

if __name__=='__main__':

    for k,i in menu.items():
        print(f'{k}:{i}')

    op = int(input('Ingresa una opción:'))

    while True:

        if op == 4:
            print("Bye")
            break
        
        elif op == 1:
            print(animales.perro)
        
        elif op == 2:
            print(animales.gato)
        
        elif op == 3:
            print(animales.camello)

        else:

            print('Opción invalida')

            for k,i in menu.items():
                print(f'{k}:{i}')

        op = int(input('Elige una opción:'))
   
   