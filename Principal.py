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
                print(f"{partes[0]}\n-> Matricula: {partes[3]}-> Idade: {partes[1]}\n-> Curso: {partes[2]}\n")
                    
            else:
                print(f"{num}", end="")

def adicionar(nome, idade, curso):
    nome = (f"{nome}").capitalize()

    with open("alunos.txt", "r") as banco:
        conteudo = banco.readlines()
        contador = 1
        for linha in conteudo:
            contador += 1
        if contador < 10:
            contador = f"000{contador}"
        elif contador < 100:
            contador = f"00{contador}"
        elif contador < 1000:
            contador = f"0{contador}"

    final = (f"{nome} ; {idade} ; {curso} ; {contador}")
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

    with open("alunos.txt", "w") as banco:
        for num in conteudo:
            banco.write(num)

    print(f"{nome} removido com sucesso")

def media_etaria():
    with open("alunos.txt", "r") as banco:
        conteudo = banco.readlines()
        somaIdades = 0
        contador = 0
        for linha in conteudo:
            if ";" in linha:
                dado = linha.split(";")
                try:
                    somaIdades += int(dado[1].strip())
                    contador += 1
                except (ValueError, IndexError):
                    continue

        if contador > 0:
            return int(somaIdades / contador)
        else:
            return 0


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
        idade = int(input("Idade: "))
        curso = input("Curso: ")

        adicionar(nome, idade, curso)
        confirmar()
    
    elif resposta == "3":
        limpar()
        print("REMOVER ALUNO\n")
        listar()
        nome = input("\nNome: ")
        matricula = input("Matricula: ")

        apagar(nome, matricula)
        confirmar()

    elif resposta == "4":
        limpar()
        print("FAIXA ETÁRIA DOS ALUNOS\n")
        FaixaEtaria = media_etaria()
        print(f"A faixa etaria dos alunos é de: {FaixaEtaria}")
        confirmar()

    elif resposta == "5":
        limpar()
        print("Programa fechado")
        break

    else:
        limpar()
        print("Digite uma alternativa válida")
        confirmar()


