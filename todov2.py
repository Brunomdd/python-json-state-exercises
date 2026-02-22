#📝 Enunciado – Sistema To-Do List com Persistência em JSON (Python)

#Desenvolva um sistema de Lista de Tarefas (To-Do List) utilizando a linguagem Python, que funcione no terminal e permita ao usuário gerenciar suas tarefas de forma simples e organizada.

#O sistema deverá possuir as seguintes funcionalidades:

#✅ 1. Adicionar tarefa

#O usuário deve informar:

#Um ID numérico inteiro positivo (não pode ser repetido).

#A descrição da tarefa (não pode estar vazia).

#Cada tarefa deve conter:

#id

#tarefas (descrição)

#concluido (status booleano: True ou False)

#O sistema deve impedir:

#IDs duplicados

#IDs negativos ou zero

#Campos vazios

#As tarefas devem ser salvas automaticamente em um arquivo JSON.

📋# 2. Listar tarefas

#O sistema deve exibir todas as tarefas cadastradas.

#Para cada tarefa, deve mostrar:

#ID

#Descrição

#Status:

#PENDENTE

#CONCLUÍDA

#Caso não existam tarefas cadastradas, o sistema deve informar ao usuário.

#✔️ 3. Concluir tarefa

#O usuário deve informar o ID da tarefa que deseja concluir.

#O sistema deve:

#Marcar a tarefa como concluída.

#Impedir que uma tarefa já concluída seja marcada novamente.

#Informar caso o ID não exista.

#Após a alteração, os dados devem ser atualizados no arquivo JSON.

#💾 4. Persistência de dados

#As tarefas devem ser armazenadas no arquivo tarefasv2.json.

#Ao iniciar o programa:

#Se o arquivo existir, os dados devem ser carregados.

#Se não existir ou estiver corrompido, o sistema deve iniciar com uma lista vazia.

#O programa deve utilizar o módulo json para leitura e escrita dos dados.

#🧠 5. Tratamento de erros

#O sistema deve:

#Validar entradas numéricas.

#Tratar exceções como:

#ValueError

#FileNotFoundError

#JSONDecodeError

#Garantir que o programa não encerre inesperadamente por erro do usuário.

📌# 6. Menu Interativo

#O sistema deve apresentar um menu com as seguintes opções:

#1 - Adicionar tarefa
#2 - Listar tarefas
#3 - Concluir tarefa
#4 - Sair

#O programa deve continuar executando até o usuário escolher sair.



import json


def leiaInt(num):
    while True:
        try:
            valor = int(input(num))
            return  valor
        except ValueError:
            print(" ❌ Erro, digite um número inteiro! ❌")


def linha(texto=42):
    return "-"* texto

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())



def carregar():
    try:
        with open("tarefasv2.json","r",encoding="utf-8") as arq:
            lista = json.load(arq)
    except (FileNotFoundError, json.JSONDecodeError):
        lista = []
    return  lista


def salvar(lista):
    with open("tarefasv2.json","w",encoding="utf-8") as arq:
        json.dump(lista,arq,ensure_ascii=False,indent=4)


def duplicador(lista,novo_id):
    for cada in lista:
        if cada["id"] == novo_id:
            return True
    return False

def validar_SN(msg):
    while True:
        valor = str(input(msg)).strip().upper()
        if valor in ("S","N"):
            return valor

def criar_tarefa(lista):
    cabecalho("Criar tarefas ⛏️")
    while True:
        id_identificador = leiaInt('digite o id: ')
        if id_identificador <= 0:
            print("❌ Erro, Só aceitamos valores positivos! ❌")
            continue
        if duplicador(lista,id_identificador):
            print("Já existe uma tarefa com esse ID")
            continue
        tarefa = input('tarefa: ')
        if not tarefa:
            print("não pode deixar vazio, digite uma tarefa")
            continue
        lista.append({"id": id_identificador, "tarefas": tarefa, "concluido": False})
        print("tarefa criada com sucesso!")
        res = validar_SN("Quer continuar? [S/N]")
        if res == "N":
            salvar(lista)
            break


def listar_tarefas(lista):
    cabecalho(" 📝 Listar Tarefas 📝")
    if not lista:
        print("Não há tarefas para mostrar!")
        return

    for v in lista:
        ativo = "CONCLUÌDA ✅" if v["concluido"] else "PENDENTE..."
        print(f"ID: {v['id']} - Tarefas: {v['tarefas']} - STATUS: {ativo}")



def concluir(lista):
    cabecalho("Concluir Tarefas ✔️")
    if not lista:
        return "Não há tarefas para concluir ⬜"
    id_identificador = leiaInt("id para concluir tarefa")

    for v in lista:
        if id_identificador == v['id']:
            if v["concluido"]:
                return 1
            else:
                v["concluido"] = True
                salvar(lista)
                return 2

    return 3

def main():
    lista = carregar()
    while True:
        cabecalho("TO DO List V2")
        print("1- Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Concluir tarefa")
        print("4 - Sair do programa")
        opc = leiaInt('escolha uma opção:')
        if opc == 1:
            criar_tarefa(lista)

        elif opc == 2:
            listar_tarefas(lista)

        elif opc == 3:
            resultado = concluir(lista)
            if resultado == 1:
                print("Erro, essa tarefa já foi concluida!! ")
            elif resultado == 2:
                print("Tarefa concluida com sucesso!")
            elif resultado == 3:
                print("Não encontramos a tarefa com esse ID")
        elif opc == 4:
            cabecalho("SAINDO DO SISTEMA . . .")
            break
        else:
            print("Valor incorreto")
    salvar(lista)

main()














