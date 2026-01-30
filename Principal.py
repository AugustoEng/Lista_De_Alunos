import os

#*DEFINIÇÕES
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def confirmar():
    nd = input()
    limpar()

def listar():
    with open("alunos.txt", "r") as banco:
        conteudo = banco.readlines()
        for num in conteudo:
            if ";" in num:
                partes = num.split(";")
                for dado in partes:
                    
                    if dado == partes[-1]:
                        dado = dado.strip()
                        print(f"{dado}", end="")
                    else:
                        dado = dado.strip()
                        print(f"{dado} - ", end="")
                print("")
            else:
                print(f"{num}", end="")

def adicionar(nome, idade, curso, matricula):
    nome = (f"{nome}").capitalize()
    final = (f"{nome} ; {idade} ; {curso} ; {matricula}")
    with open("alunos.txt", "a") as banco:
        banco.write(f"{final}\n")
        print(f"{nome} Adicionado com sucesso")
            
def apagar(nome, matricula):
    with open("alunos.txt", "r") as banco:
        conteudo = banco.readlines()
        indice = 0
        nome = f"{nome}".strip().capitalize()
        matricula = f"{matricula}".strip()

        for num in conteudo:
            if nome and matricula in num:
                conteudo.pop(indice)

    with open("aunos.txt", "w") as banco:
        for num in conteudo:
            banco.write(num)

    print(f"{nome} removido com sucesso")


try:
    with open("alunos.txt", "r") as chamada:
        pass
except FileNotFoundError:
    with open("alunos.txt", "w") as chamadas:
        pass

while True:
    limpar()
    print("EXTRATO BANCÁRIO\n")
    print("[1] Ver Lista de chamada")
    print("[2] Adicionar Aluno")
    print("[3] Remover Aluno")
    print("[4] Mostrar Média Etária")
    print("[5] Sair")
    resposta = input("\nResposta: ")

    if resposta == "1":
        limpar()
        listar()
        confirmar()

    elif resposta == "2":
        limpar()
        print("ADICIONAR ALUNO\n")
        nome = input("Nome: ")
        while True: 
            idade = input("Idade: ")
            if idade != int:
                limpar()
                print("Digite um numeru válido")
            else:
                break
        curso = input("Curso: ")
        matricula = input("Matricula: ")

        adicionar(nome, idade, curso, matricula)
        confirmar()
    
    elif resposta == "3":
        limpar()
        print("REMOVER ALUNO\n")
        listar()
        nome = input("\nNome: ")
        matricula = input("Matricula: ")

        apagar(nome, matricula)
        confirmar()



