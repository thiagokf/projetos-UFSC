class Pilha():
    def __init__(self, limite):
        self.__limite = limite
        self.__pilha = []

    def push(self, dado):
        if len(self.__pilha) < self.__limite:
            self.__pilha.append(dado)

        else:
            print ("ta cheio")

    def pop(self):
        tira = len(self.__pilha) - 1
        self.__pilha.pop(tira)

    def top(self):
        if len(self.__pilha) == 0:
            return print("pilha vazia")
        print(self.__pilha[len(self.__pilha) - 1])


p1 = Pilha(2)

p1.push(12)
p1.push(21)
p1.push(23)
p1.top()
p1.pop()
p1.top()
