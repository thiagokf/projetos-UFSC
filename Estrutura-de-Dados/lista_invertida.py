# lista invertida para clubes de futebol
class Diretorio:
    def __init__(self):
        self.__diretorio = {}

    @property
    def diretorio(self):
        return self.__diretorio
    
    # verifica se a chave secundaria já existe no diretório
    def verifica_atributo(self, chave):
        if chave not in self.__diretorio:
            self.__diretorio[chave] = []

    # insere o index do registro na lista correspondente a chave secundaria
    def inserir(self, chave, index):
        self.verifica_atributo(chave)
        self.__diretorio[chave].append(index)

    # busca os indices associados a chave secundaria
    def buscar_atributo(self, chave):
        dir = self.__diretorio.get(chave, [])
        return dir
    
    # exclui o index do registro da lista correspondente a chave secundaria
    def excluir(self, chave, index):
        if chave in self.__diretorio:
            if index in self.__diretorio[chave]:
                self.__diretorio[chave].remove(index)
                if not self.__diretorio[chave]: # remove a chave secundaria se a lista ficar vazia
                    del self.__diretorio[chave]

# diretorio com faixas continuas já programadas
class DiretorioContinuo:
    def __init__(self):
        self.__diretorio = {'0 a 10': [], '11 a 20': [], '21 a 30': [], '+ de 30': []}
    
    @property
    def diretorio(self):
        return self.__diretorio
    
    # verifica a faixa da chave secundaria
    def verifica_faixa(self, chave):
        if chave <= 10:
            faixa = '0 a 10'
        elif chave <= 20:
            faixa = '11 a 20'
        elif chave <= 30:
            faixa = '21 a 30'
        else:
            faixa = '+ de 30'
        return faixa
    
    # insere o index do registro na lista correspondente a faixa da chave secundaria
    def inserir(self, chave, index):
        faixa = self.verifica_faixa(chave)
        self.__diretorio[faixa].append(index)
    
    # exclui o index do registro da lista correspondente a faixa da chave secundaria
    def excluir(self, chave, index):
        faixa = self.verifica_faixa(chave)
        if index in self.__diretorio[faixa]:
            self.__diretorio[faixa].remove(index)

    # busca os indices associados a faixa da chave secundaria
    def buscar_atributo(self, chave):
        dir = self.__diretorio.get(chave, [])
        return dir

class listaInvertida:
    def __init__(self, diretorio=None):
        self.__dados = []

    @property
    def dados(self):
        return self.__dados
    
    # insere um novo time na lista e atualiza os diretórios
    def inserir_elemento(self, id, nome, titulos, estado, divisao, cor, dir_titulos, dir_estado, dir_divisao, dir_cor):
        time = {
            'id': id,
            'nome': nome,
            'titulos': titulos,
            'estado': estado,
            'divisao': divisao,
            'cor': cor
        }
        self.__dados.append(time)
        dir_titulos.inserir(titulos, id)
        dir_estado.inserir(estado, id)
        dir_divisao.inserir(divisao, id)
        dir_cor.inserir(cor, id)
    
    # busca por id do time
    def buscar_elemento(self, id):
        for i, time in enumerate(self.__dados):
            if time['id'] == id:
                return time, i
        return None
    
    # busca todos os times que possuem o valor especifico em um atributo
    def busca_especifica(self, dir_atributo, valor):
        elementos = dir_atributo.buscar_atributo(valor)
        for i in elementos:
            self.buscar_elemento(i)
            print(self.buscar_elemento(i))
    
    def buscar_todos(self):
        for time in self.__dados:
            print(time)
    
    # exclui um time da lista e atualiza os diretórios
    def excluir_elemento(self, id, dir_titulos, dir_estado, dir_divisao, dir_cor):
        time, i = self.buscar_elemento(id)
        if time is None:
            return False
        dir_titulos.excluir(time['titulos'], id)
        dir_estado.excluir(time['estado'], id)
        dir_divisao.excluir(time['divisao'], id)
        dir_cor.excluir(time['cor'], id)
        del self.__dados[i]
        return True

    def busca_combinada(self, dir1, cond1, dir2, cond2):
        resultados1 = set(dir1.buscar_atributo(cond1))
        resultados2 = set(dir2.buscar_atributo(cond2))
        resultados_combinados = resultados1.intersection(resultados2)
        for i in resultados_combinados:
            print(lista.buscar_elemento(i))


# Exemplo de uso
lista = listaInvertida()
dir_titulos = DiretorioContinuo()
dir_estado = Diretorio()
dir_divisao = Diretorio()
dir_cor = Diretorio()

lista.inserir_elemento('1', 'Vasco', 43, 'RJ', 'A', 'Alvinegro', dir_titulos, dir_estado, dir_divisao, dir_cor)
lista.inserir_elemento('2', 'Corinthias', 25, 'SP', 'A', 'Alvinegro', dir_titulos, dir_estado, dir_divisao, dir_cor)
lista.inserir_elemento('3', 'Palmeiras', 32, 'SP', 'A', 'Verde', dir_titulos, dir_estado, dir_divisao, dir_cor)
lista.inserir_elemento('4', 'Cruzeiro', 29, 'MG', 'A', 'Azul', dir_titulos, dir_estado, dir_divisao, dir_cor)
lista.inserir_elemento('5', 'Coritiba', 25, 'PR', 'A', 'Verde', dir_titulos, dir_estado, dir_divisao, dir_cor)
lista.inserir_elemento('6', 'Chapecoence', 25, 'SC', 'A', 'Verde', dir_titulos, dir_estado, dir_divisao, dir_cor)
lista.inserir_elemento('7', 'Avai', 22, 'SC', 'B', 'Azul', dir_titulos, dir_estado, dir_divisao, dir_cor)
lista.inserir_elemento('8', 'Flamengo', 35, 'RJ', 'A', 'Vermelho', dir_titulos, dir_estado, dir_divisao, dir_cor)
lista.inserir_elemento('9', 'Criciuma', 28, 'SC', 'B', 'Amarelo', dir_titulos, dir_estado, dir_divisao, dir_cor)
lista.inserir_elemento('10', 'Figueirence', 20, 'SC', 'C', 'Alvinegro', dir_titulos, dir_estado, dir_divisao, dir_cor)
lista.inserir_elemento('11', 'Botafogo', 30, 'RJ', 'A', 'Alvinegro', dir_titulos, dir_estado, dir_divisao, dir_cor)
lista.inserir_elemento('12', 'Santos', 22, 'SP', 'A', 'Alvinegro', dir_titulos, dir_estado, dir_divisao, dir_cor)
lista.inserir_elemento('13', 'Gremio', 18, 'RS', 'A', 'Azul', dir_titulos, dir_estado, dir_divisao, dir_cor)
lista.inserir_elemento('14', 'Internacional', 19, 'RS', 'A', 'Vermelho', dir_titulos, dir_estado, dir_divisao, dir_cor)
lista.inserir_elemento('15', 'Atletico-MG', 27, 'MG', 'A', 'Alvinegro', dir_titulos, dir_estado, dir_divisao, dir_cor)
lista.inserir_elemento('16', 'Atletico-PR', 15, 'PR', 'A', 'Vermelho', dir_titulos, dir_estado, dir_divisao, dir_cor)
lista.inserir_elemento('17', 'Juventude', 21, 'RS', 'B', 'Verde', dir_titulos, dir_estado, dir_divisao, dir_cor)
lista.inserir_elemento('18', 'Atletico-Mineiro', 21, 'MG', 'B', 'Verde', dir_titulos, dir_estado, dir_divisao, dir_cor)
'''
print('-----------testes de busca de todos------------------')
# mostrar todos os dados
lista.buscar_todos()
print()
print('-----------testes de busca por Id------------------')
# testes de busca
print(lista.buscar_elemento('3'))  # retorna os dados do Palmeiras
print(lista.buscar_elemento('10'))  # retorna os dados do Figueirence
print(lista.buscar_elemento('20'))  # retorna None (time não existe)
print()
print('-----------testes de exclusão------------------')
# testes de exclusão
print(lista.buscar_elemento('8'))
lista.excluir_elemento('8', titulos, estado, divisao, cor)  # Exclui o Flamengo (aqui é vasco)
print(lista.buscar_elemento('8'))  # retorna None (time não existe)

print()
print('-----------testes de busca por atributo------------------')
# testes de busca por atributo
lista.busca_especifica(estado, 'SP')  # Deve retornar os dados dos times de SP
print('-----------------------------------')
lista.busca_especifica(cor, 'Alvinegro')  # Deve retornar os dados dos times Alvinegros
print()
print('-----------testes de busca combinada------------------')
# testes de busca combinada
print('----------------RJ e Alvinegro-------------------')
lista.busca_combinada(estado, 'RJ', cor, 'Alvinegro')  # Exemplo de busca combinada entre estado e cor
print('----------------Divisao A e Verde-------------------')
lista.busca_combinada(divisao, 'A', cor, 'Verde')  # Exemplo de busca combinada entre divisão e cor
print('----------------Entre 21 a 30 titulos e MG-------------------')
lista.busca_combinada(titulos, '21 a 30', estado, 'MG')  # Exemplo de busca combinada entre títulos e estado
'''
def exibir_menu():
    print("\n" + "="*40)
    print("⚽ Sistema de Lista Invertida de Clubes ⚽")
    print("="*40)
    print("1. Inserir Novo Clube")
    print("2. Buscar Clube por ID")
    print("3. Buscar Clubes por Atributo Específico")
    print("4. Buscar Clubes com Condição Combinada (E/AND)")
    print("5. Excluir Clube por ID")
    print("6. Listar Todos os Clubes")
    print("0. Sair")
    print("-" * 40)

def obter_dados_clube():
    print("\n--- Inserir Novo Clube ---")
    
    id = input("ID do Clube: ").strip()
    nome = input("Nome do Clube: ").strip()
    titulos = int(input("Número de Títulos: ").strip())
    estado = input("Estado (Ex: SP, RJ, MG): ").strip().upper()
    divisao = input("Divisão (Ex: A, B, C, D): ").strip().upper()
    cor = input("Cor Predominante: ").strip().capitalize()
    
    return id, nome, titulos, estado, divisao, cor

while True:
        exibir_menu()
        
        try:
            opcao = input("Escolha uma opção: ")
            
            if opcao == '1':
                id, nome, titulos, estado, divisao, cor = obter_dados_clube()
                lista.inserir_elemento(id, nome, titulos, estado, divisao, cor, dir_titulos, dir_estado, dir_divisao, dir_cor)
                print(f"\nClube '{nome}' inserido com ID: {id}.")

            elif opcao == '2':
                try:
                    id_busca = (input("\nID do clube a buscar: "))
                    clube= lista.buscar_elemento(id_busca)
                    print(clube)
                    if clube:
                        print(f"Clube encontrado com ID {id_busca}")
                    else:
                        print(f"\nClube com ID {id_busca} não encontrado.")
                except ValueError:
                    print(f"\nClube com ID {id_busca} não encontrado.")

            elif opcao == '3':
                op = input("\nEscolha o atributo para busca específica:\n1. Títulos\n2. Estado\n3. Divisão\n4. Cor\nOpção: ")
                if op == '1':
                    dir = dir_titulos
                if op == '2':
                    dir = dir_estado
                if op == '3':
                    dir = dir_divisao
                if op == '4':
                    dir = dir_cor
                valor = input("Digite o valor do atributo para busca (estado e divisão em maiusculo): ")
                lista.busca_especifica(dir, valor)

            elif opcao == '4':
                op1 = input("\nEscolha o atributo para busca específica:\n1. Títulos\n2. Estado\n3. Divisão\n4. Cor\nOpção: ")
                if op1 == '1':
                    dir1 = dir_titulos
                if op1 == '2':
                    dir1 = dir_estado
                if op1 == '3':
                    dir1 = dir_divisao
                if op1 == '4':
                    dir1 = dir_cor
                cond1 = input("valor: ")
                
                op2 = input("\nEscolha o atributo para busca específica:\n1. Títulos\n2. Estado\n3. Divisão\n4. Cor\nOpção: ")
                if op2 == '1':
                    dir2 = dir_titulos
                if op2 == '2':
                    dir2 = dir_estado
                if op2 == '3':
                    dir2 = dir_divisao
                if op2 == '4':
                    dir2 = dir_cor
                cond2 = input("valor: ")
                lista.busca_combinada(dir1, cond1, dir2, cond2)

            elif opcao == '5':
                try:
                    id = (input("\nID do clube a excluir: "))
                    if lista.excluir_elemento(id, dir_titulos, dir_estado, dir_divisao, dir_cor):
                        print(f"\nClube com ID {id} excluído com sucesso e diretórios atualizados.")
                    else:
                        print(f"\nClube com ID {id} não encontrado para exclusão.")
                except ValueError:
                    print("\nID inválido. Digite um número inteiro.")

            elif opcao == '6':
                lista.buscar_todos()

            elif opcao == '0':
                print("\nEncerrando o sistema")
                break
                
            else:
                print("\nOpção inválida. Por favor, escolha um número de 0 a 6.")

        except Exception as e:
            print(f"\nOcorreu um erro inesperado: {e}")
