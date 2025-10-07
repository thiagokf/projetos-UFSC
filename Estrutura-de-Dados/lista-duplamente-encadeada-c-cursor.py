class Elemento:
    def __init__(self, valor):
            self.__valor = valor
            self.__ant = None
            self.__prox = None
            self.__posicao = None

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

    @property
    def ant(self):
        return self.__ant

    @ant.setter
    def ant(self, ant):
        self.__ant = ant

    @property
    def posicao(self):
        return self.__posicao

    @posicao.setter
    def posicao(self, posicao):
        self.__posicao = posicao

class Cursor:
    def __init__(self):
        self.__posicao = 0
        self.__aponta = None

    @property
    def posicao(self):
        return self.__posicao

    @posicao.setter
    def posicao(self, posicao):
        self.__posicao = posicao

    @property
    def aponta(self):
        return self.__aponta

    @aponta.setter
    def aponta(self, aponta):
        self.__aponta = aponta

class ListaEncadeada:
    def __init__(self, tamanho):
        self.__tamanho = tamanho
        self.__cursor = Cursor()
        self.__tamanho_atual = 0
        self.__inicio = None
        self.__fim = None

    @property
    def tamanho(self):
        return self.__tamanho

    @tamanho.setter
    def tamanho(self, tamanho):
        self.__tamanho = tamanho

    @property
    def tamanho_atual(self):
        return self.__tamanho_atual

    @tamanho_atual.setter
    def tamanho_atual(self, tamanho_atual):
        self.__tamanho_atual = tamanho_atual

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

    @property
    def cursor(self):
        return self.__cursor

    @cursor.setter
    def cursor(self, cursor):
        self.__cursor = cursor

    def ajuste_de_posicao_mais(self, i):
        while True:
                i.posicao += 1
                if i.prox == None:
                    return
                i = i.prox

    def ajuste_de_posicao_menos(self, i):
        while True:
                i.posicao -= 1
                if i.prox == None:
                    return
                i = i.prox

    def inserir_antes_do_atual(self, elemento):
        self.__tamanho_atual += 1
        atual = self.__cursor.aponta
        if atual == None:
            self.__inicio = elemento
            self.__fim = elemento
            self.__cursor.aponta = elemento
            elemento.posicao = 1
            return
        if atual.ant == None:
            elemento.prox = self.__inicio
            self.__inicio = elemento
            elemento.posicao = 1
            atual.ant = elemento
            self.ajuste_de_posicao_mais(atual)
            return
        atual.ant.prox = elemento
        elemento.ant = atual.ant
        atual.ant = elemento
        elemento.prox = atual
        elemento.posicao = atual.posicao
        self.ajuste_de_posicao_mais(atual)

    def inserir_depois_do_atual(self, elemento):
        self.__tamanho_atual += 1
        atual = self.__cursor.aponta
        if atual == None:
            self.__inicio = elemento
            self.__fim = elemento
            elemento.posicao = 1
            return
        if atual.prox == None:
            self.__fim = elemento
        elemento.posicao = atual.posicao + 1
        elemento.prox = atual.prox
        if elemento.prox != None:
            elemento.prox.ant = elemento
        atual.prox = elemento
        elemento.ant = atual
        if elemento.prox != None:
            self.ajuste_de_posicao_mais(elemento.prox)
        return

    def inserir_como_primeiro(self, elemento):
        if self.__tamanho_atual + 1 <= self.__tamanho:
            self.ir_para_primeiro()
            self.inserir_antes_do_atual(elemento)
        else:
            print("lista cheia")

    def inserir_como_ultimo(self, elemento):
        if self.__tamanho_atual + 1 <= self.__tamanho:
            self.ir_para_ultimo()
            self.inserir_depois_do_atual(elemento)
        else:
            print("lista cheia")

    def inserir_na_posicao(self, k, elemento):
        if self.__tamanho_atual + 1 <= self.__tamanho:
            self.ir_para_primeiro()
            self.avancar_k_posicoes(k-1)
            self.inserir_antes_do_atual(elemento)
            self.__cursor.aponta = elemento
        else:
            print("lista cheia")

    def excluir_atual(self):
        if self.__tamanho_atual > 0:
            i = self.__cursor.aponta.prox
            if i == None:
                self.__cursor.aponta.ant.prox = None
                self.__fim = self.__cursor.aponta.ant
            else:
                i.ant = self.__cursor.aponta.ant
                if i.ant == None:
                    self.__inicio = i
                else:
                    self.__cursor.aponta.ant.prox = i
                self.ajuste_de_posicao_menos(i)
            self.__cursor.aponta.prox = None
            self.__cursor.aponta.ant = None
            self.__cursor.aponta.posicao = None
            self.__tamanho_atual -= 1
        else:
            print('lista vazia')

    def excluir_primeiro(self):
        if self.__tamanho_atual > 0:
            self.ir_para_primeiro()
            self.excluir_atual()
        else:
            print("Lista Vazia")

    def excluir_ultimo(self):
        if self.__tamanho_atual > 0:
            self.ir_para_ultimo()
            self.excluir_atual()
        else:
            print("Lista Vazia")

    def buscar(self, elemento):
        self.ir_para_primeiro()
        while True:
            if elemento == self.__cursor.aponta:
                return True
            if self.__cursor.aponta.prox == None:
                break
            self.avancar_k_posicoes(1)
        return False

    def ir_para_ultimo(self):
        self.__cursor.posicao = self.__tamanho_atual
        self.__cursor.aponta = self.__fim

    def ir_para_primeiro(self):
        self.__cursor.posicao = 1
        self.__cursor.aponta = self.__inicio

    def avancar_k_posicoes(self, k):
        if self.__cursor.posicao + k <= self.__tamanho:
            self.__cursor.posicao += k
            while True:
                if self.__cursor.aponta.posicao == self.__cursor.posicao:
                    return self.__cursor.aponta
                self.__cursor.aponta = self.__cursor.aponta.prox
        else:
            print("Deu erro jão")
    def retroceder_k_posicoes(self, k):
        if self.__cursor.posicao - k > 0:
            self.__cursor.posicao -= k
            while True:
                if self.__cursor.aponta.posicao == self.__cursor.posicao:
                    return
                self.__cursor.aponta = self.__cursor.aponta.ant
        else:
            print("Deu erro jão")
    def acessar_atual(self):
        return self.__cursor.aponta

    
# inserindo como primeiro (OK!)
# inserindo como ultimo (Ok!)
# inserindo depois do apontado (Ok!)
# inserindo antes do apontado (Ok!)
# inserir na posicao (Ok!)
# excluir atual (Ok!)
# excluir primeiro (Ok!)
# excluir ultimo (Ok!)
# buscar (Ok!)

# # cursor
# avançar k posicoes (ok!)
# retroceder k posicoes (ok!)
a = ListaEncadeada(5)
n = Elemento('niki')
t = Elemento('thiago')
ni = Elemento('nikinha')
c = Elemento('triangulo')
p = Elemento('bola')
v = Elemento('dsa')

a.inserir_como_primeiro(n)
a.inserir_como_primeiro(ni)
a.inserir_como_ultimo(t)
a.inserir_como_ultimo(c)
print(a.acessar_atual().valor)
a.retroceder_k_posicoes(3)
print(a.acessar_atual().valor)
a.inserir_depois_do_atual(p)
print('--nikinha--')
print(ni.posicao)
print(ni.ant)
print(ni.prox.valor)
print('--niki--')
print(n.posicao)
print(n.ant.valor)
print(n.prox.valor)
print('--bola--')
print(p.posicao)
print(p.ant.valor)
print(p.prox.valor)
print('--thiago--')
print(t.posicao)
print(t.ant.valor)
print(t.prox.valor)
print('--thiangulo--')
print(c.posicao)
print(c.ant.valor)
print(c.prox)

print(a.buscar(p))
