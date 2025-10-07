class Elemento:
    def __init__(self, valor):
            self.__valor = valor
            self.__prox = None

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @property
    def prox(self):
        return self.__prox

    @prox.setter
    def prox(self, prox):
        self.__prox = prox

class Fila:
    def __init__(self):
        self.__inicio = None
        self.__fim = None
    
    @property
    def inicio(self):
        return self.__inicio
    
    @inicio.setter
    def inicio(self, inicio):
        self.__inicio = inicio
    
    @property
    def fim(self):
        return self.__fim
    
    @fim.setter
    def fim(self, fim):
        self.__fim = fim

    def entrar(self, valor):
        novo = Elemento(valor)
        if self.__inicio == None:
            self.__inicio = novo
            self.__fim = novo
            return
        self.__fim.prox = novo
        self.__fim = novo
    
    def sair(self):
        if self.__fim == None:
            print("fila vazia")
            return
        if self.__inicio.prox == None:
           self.__inicio = None
           self.__fim = None
           print("fila vazia")
           return
        self.__inicio = self.__inicio.prox

f = Fila()
f.sair()
# Teste entrar na fila (OK!)
f.entrar("bolinha")
f.entrar("quadrado")
f.entrar("triangulo")
print(f"inicio: {f.inicio.valor}")
print(f"proximo: {f.inicio.prox.valor}")
print(f"fim: {f.fim.valor}")

print("-------------------------")
# Teste sair da fila
f.sair()
print(f"inicio: {f.inicio.valor}")
print(f"proximo: {f.inicio.prox.valor}")
print(f"fim: {f.fim.valor}")

print(("---|saiu|---"))
f.sair()
print(f"inicio: {f.inicio.valor}")
print(f"fim: {f.fim.valor}")

print(("---|saiu|---"))
f.sair()
print(f"inicio: {f.inicio}")
print(f"fim: {f.fim}")
