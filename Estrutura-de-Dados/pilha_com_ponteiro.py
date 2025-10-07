class Elemento:
    def __init__(self, valor):
            self.__valor = valor
            self.__ant = None

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @property
    def ant(self):
        return self.__ant

    @ant.setter
    def ant(self, ant):
        self.__ant = ant

class Pilha:
    def __init__(self):
        self.__topo = None
    
    @property
    def topo(self):
        return self.__topo
    
    def push(self, valor):
        novo = Elemento(valor)
        if self.__topo == None:
            self.__topo = novo
            return
        else:
            novo.ant = self.__topo
            self.__topo = novo

    def pop(self):
        if self.__topo == None:
            print("Não tem topo jão")
            return
        if self.__topo.ant == None:
            self.__topo = None
            return
        self.__topo = self.__topo.ant


p = Pilha()
e = Elemento("bola")
print(e.ant)
# testando adicionando os Elementos (OK!)
p.push("bolinha")
p.push("quadrado")
p.push("triangulo")
print(p.topo.valor)
print(p.topo.ant.valor)
print(p.topo.ant.ant.valor)

# teste popando os Elementos (OK!)
print("----------------------------------------")
p.pop()
print(p.topo.valor)
print(p.topo.ant.valor)
p.pop()
print(p.topo)
p.pop()
print(p.topo)
p.pop()
