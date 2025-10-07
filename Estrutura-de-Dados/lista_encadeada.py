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
    
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

class Lista:
    def __init__(self, tamanho):
        self.__tamanho = tamanho
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
    

    def inserir_como_primeiro(self, elemento):
        if self.__tamanho_atual + 1 <= self.__tamanho:
            elemento.prox = self.__inicio
            self.__inicio = elemento
            elemento.posicao = 1
            if self.__tamanho_atual > 0:
                i = self.__inicio.prox
                while True:
                    i.posicao += 1
                    if i.prox == None:
                        self.__fim = i
                        break
                    i = i.prox
            self.__tamanho_atual += 1
        else:
            print("Lista Cheia")

    def inserir_como_ultimo(self, elemento):
        if self.__tamanho_atual + 1 <= self.__tamanho:
            self.__tamanho_atual += 1
            self.__fim.prox = elemento
            self.__fim = elemento
            elemento.posicao = self.__tamanho_atual
            return
        else:
            print("lista cheia")
    
    def inserir_na_posicao(self, posicao, elemento):
        if self.__tamanho_atual + 1 <= self.__tamanho:
            if posicao == 1:
                self.inserir_como_primeiro(elemento)
                return
            i = self.__inicio
            while i is not None:
                if i.posicao == posicao - 1:
                    elemento.prox = i.prox
                    i.prox = elemento
                    elemento.posicao = posicao
                    self.__tamanho_atual += 1
                    # Atualiza posições dos próximos
                    proximo = elemento.prox
                    while proximo is not None:
                        proximo.posicao += 1
                        proximo = proximo.prox
                    break
                i = i.prox

    def inserir_depois_de(self, ref, elemento):
        if self.__tamanho_atual + 1 <= self.__tamanho:
            i = self.__inicio
            while True:
                if ref == i:
                    elemento.prox = i.prox
                    elemento.posicao = i.posicao + 1
                    proximo = i.prox
                    i.prox = elemento
                    while True:
                        proximo.posicao += 1
                        if proximo.prox == None:
                            break
                        proximo = proximo.prox
                if i.prox == None:
                    print("referencia nao encontrada")
                    return
                i = i.prox
    
    def inserir_antes_de(self, ref, elemento):
        if self.__tamanho_atual + 1 <= self.__tamanho:
            i = self.__inicio
            if ref == i:
                 self.inserir_como_primeiro(elemento)
                 return 
            i = self.__inicio.prox 
            while True:
                if i.prox == ref:
                    elemento.prox = i.prox
                    elemento.posicao = i.prox.posicao
                    proximo = i.prox
                    i.prox = elemento
                    while True:
                        proximo.posicao += 1
                        if proximo.prox == None:
                            return
                        proximo = proximo.prox
                if i.prox == None:
                    print("referencia nao encontrada")
                    return
                print(i.valor)
                i = i.prox

    def remover_primeiro(self):
        if self.__tamanho_atual > 0:
            self.__inicio = self.__inicio.prox
            i = self.__inicio
            while True:
                i.posicao -= 1
                if i.prox == None:
                    break
                i = i.prox
    
    def remover_da_posicao(self, posicao):
        if self.__tamanho_atual > 0:
            if posicao == 1:
                self.remover_primeiro()
                return
            i = self.__inicio
            while True:
                if i.prox.posicao == posicao:
                    print(i.prox.valor)
                    proximo = i.prox.prox
                    i.prox.prox = None
                    i.prox.posicao = None
                    i.prox = proximo
                    while True:
                        proximo.posicao -= 1
                        if proximo.prox == None:
                            return
                        proximo = proximo.prox
                if i.prox == None:
                    print("deu boga")
                    return
                i = i.prox
    
    def remover(self, ref):
        if self.__tamanho_atual > 0:
            if ref == self.__inicio:
                self.remover_primeiro()
                return
            i = self.__inicio
            
            while True:
                if i.prox == ref:
                    proximo = i.prox.prox
                    i.prox.prox = None
                    i.prox.posicao = None
                    i.prox = proximo
                    while True:
                        proximo.posicao -= 1
                        if proximo.prox == None:
                            
                            return
                        proximo = proximo.prox
                if i.prox == None:
                    print("deu boga")
                    return
                i = i.prox

quad = Elemento('quadrado')
trig = Elemento('triangulo')
bola = Elemento('bola')
p = Elemento('p')
q = Elemento('q')
n = Elemento('niki')
a = Lista(6)
b = Elemento('te amo amor')
# inserindo como primeiro (OK!)
a.inserir_como_primeiro(quad)
a.inserir_como_primeiro(trig)
print(a.inicio.valor)
print(a.inicio.prox)
print('--')
print(trig.posicao)
print(quad.posicao)
print(trig.prox.valor)
print(a.tamanho_atual)
print(a.fim.valor)
print("--posicoes--")
print(quad.posicao)
print(trig.posicao)
print("--")
# inserindo como ultimo
a.inserir_como_ultimo(bola)
print(bola.posicao)
print(a.fim.valor)

print("--posicoes--")
print(bola.posicao)
print(quad.posicao)
print(trig.posicao)
print('--')
print('-------------inserindo na posicao------------')
a.inserir_na_posicao(2, p)
print('---blocos---')
print("--triangulo--")
print(trig.posicao)
print(trig.prox.valor)
print("--p--")
print(p.posicao)
print(p.prox.valor)
print("--quadrado--")
print(quad.posicao)
print(quad.prox.valor)
print("--bola--")
print(bola.posicao)
print(bola.prox)


print("inserindo depois de (OK)")
a.inserir_depois_de(quad, q)

print('---blocos---')
print("--triangulo--")
print(trig.posicao)
print(trig.prox.valor)
print("--p--")
print(p.posicao)
print(p.prox.valor)
print("--q--")
print(q.posicao)
print(q.prox.valor)
print("--bola--")
print(bola.posicao)
print(bola.prox)


print('========= inserindo antes de no troca toca') #fodase (OK!)
a.inserir_antes_de(quad ,n)

print('---blocos---')
print("--triangulo--")
print(trig.posicao)
print(trig.prox.valor)
print("--p--")
print(p.posicao)
print(p.prox.valor)
print('--n--')
print(n.posicao)
print(n.prox.valor)
print("--quadrado--")
print(quad.posicao)
print(quad.prox.valor)
print("--bola--")
print(bola.posicao)
print(bola.prox)
print("--q--")
print(q.posicao)
print(q.prox.valor)


# remocao do primeiro (OK!)
print('-----removendo o primeiro----')
print(a.inicio.valor)
a.remover_primeiro()
print(a.inicio.valor)
print('---blocos---')
print("--p--")
print(p.posicao)
print(p.prox.valor)
print('--n--')
print(n.posicao)
print(n.prox.valor)
print("--quadrado--")
print(quad.posicao)
print(quad.prox.valor)
print("--bola--")
print(bola.posicao)
print(bola.prox)
print("--q--")
print(q.posicao)
print(q.prox.valor)

# removendo pela posicao (ok!)
print('-----removendo pela posicao----')
a.remover_da_posicao(3)

print('---blocos---')
print("--p--")
print(p.posicao)
print(p.prox.valor)
print('--n--')
print(n.posicao)
print(n.prox.valor)
print("--q--")
print(q.posicao)
print(q.prox.valor)
print("--bola--")
print(bola.posicao)
print(bola.prox)
# removendo por referencia

a.remover(q)
print('-----removendo por ref-----')
print('---blocos---')
print("--p--")
print(p.posicao)
print(p.prox.valor)
print('--n--')
print(n.posicao)
print(n.prox.valor)
print("--q--")
print(q.posicao)
print(q.prox.valor)
print("--bola--")
print(bola.posicao)
print(bola.prox)
