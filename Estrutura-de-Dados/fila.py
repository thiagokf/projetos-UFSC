class Fila:
    def __init__(self):
        self.__fila = []
    
    @property
    def fila(self):
        return self.__fila
    
    def entrar(self, dado):
        self.__fila.append(dado)
    
    def sair(self):
        if len(self.__fila) > 0:
            self.__fila.pop(0)
        else:
            return "erro! fila vazia"

    def frente(self):
        if len(self.__fila) > 0:
            return self.__fila[0]
        else:
            return "erro! fila vazia"

f = Fila()

f.entrar(10)
f.entrar(30)
print(f.fila)
f.entrar(23)
print(f.frente())
f.sair()

print(f.frente())

# -----> Fila em Ciclo (mais eficiente) <-----

class Fila:
    def __init__(self, tamanho):
        self.__tamanho = tamanho
        self.__inicio = 0
        self.__fim = 0
        self.__fila = [None] * tamanho

    @property
    def fila(self):
        return self.__fila

    def entrar(self, dado):
        if self.__fila[self.__fim] == None:
            self.__fila[self.__fim] = dado
            self.__fim += 1
            if self.__fim == self.__tamanho:
                self.__fim = 0
        else:
            print ("fila cheia")
            
    def sair(self):
        if self.__fila[self.__inicio] == None:
            print("lista vazia jão")
            return
        else:
            self.__fila[self.__inicio] = None
            self.__inicio += 1
            if self.__inicio == self.__tamanho:
                self.__inicio = 0

    def frente(self):
        if self.__fila[self.__inicio] == None:
            print("lista vazia jão")
            return
        return self.__fila[self.__inicio]
    
f = Fila(5)
# tentando tirar lista vazia (ok!)
f.sair()
f.frente()
# fazendo a fila (ok!)
f.entrar(2)
print(f.fila)
f.entrar(3)
f.entrar(7)
f.entrar(55)
f.entrar(5)
print(f.fila)

# tentando adicionar na fila cheia (ok!)
f.entrar(5)

# saindo da fila (ok!)
f.sair()
print(f.fila)

# adicionando (ok!)
f.entrar(4)
print(f.fila)

# verificando se a frente ta certa (ok!)
print(f.frente())

# outros testes
f.sair()
print(f.fila)
f.entrar(0)
print(f.fila)
print(f.frente())
