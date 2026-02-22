#Exercício: Gerenciador de Tarefas (TO DO List) em Python com JSON

#Objetivo:
#Criar um programa em Python que funcione como uma lista de tarefas (TO DO List), permitindo ao usuário adicionar, remover e listar tarefas. As tarefas devem ser salvas em um arquivo JSON, garantindo que as informações sejam preservadas entre execuções do programa.

#Requisitos do programa:

#Menu Interativo
#Ao iniciar, o programa deve exibir um menu com as opções:

#Adicionar tarefa

#Remover tarefa

#Listar tarefas

#Encerrar o programa

#Adicionar tarefa

#Permitir que o usuário insira o nome de uma tarefa.

#Exibir uma mensagem de confirmação após a tarefa ser adicionada.

#Remover tarefa

#Permitir que o usuário remova uma tarefa escolhendo pelo número correspondente na lista.

#Validar entradas, garantindo que sejam números positivos e correspondam a tarefas existentes.

#Exibir uma mensagem de confirmação após a remoção.

#Listar tarefas

#Exibir todas as tarefas numeradas ou informar que não há tarefas se a lista estiver vazia.

#Persistência com JSON

#Carregar a lista de tarefas do arquivo todo.json ao iniciar o programa.

#Salvar alterações (adições ou remoções) no arquivo ao encerrar o programa.

#Validação de entradas

#Garantir que entradas numéricas sejam válidas.

#Tratar erros de forma amigável para o usuário.

#Aparência e usabilidade

#Usar cabeçalhos e linhas de separação para organizar o menu e listas.

#Incluir pausas (sleep) para melhorar a experiência visual.


import json
from time import sleep

def linha(txt=42):
    return "-" * txt

def cabecalho(msg):
    print(linha())
    print(msg.center(42))
    print(linha())

def leiaInt(valor):
    while True:
        try:
            m = int(input(valor))
            return m
        except ValueError:
            print("Erro, Só aceitamos valores inteiros!")

def carregar():
    try:
        with open("todo.json","r",encoding="utf-8")as arq:
            lista = json.load(arq)
    except FileNotFoundError:
        lista = []
    return  lista

def salvar(lista):
    with open("todo.json","w",encoding="utf-8") as arq:
        json.dump(lista, arq, ensure_ascii=False, indent=4)



def listar_tarefas(lista):
    cabecalho("Listando Tarefas...")
    sleep(1)
    if not lista:
        print("Não há tarefas para mostrar!")
        return
    for pos,valor in enumerate(lista,start=1):
        print(f"{pos} - {valor}")

def main():
    lista = carregar()
    while True:
        cabecalho("TO DO List usando JSON V1 ")
        print("1- Adicionar tarefa")
        print("2- Remover tarefa")
        print("3- Listar tarefas")
        print("4 - Encerrar o programa")

        opc = leiaInt('Escolha uma opção: ')
        if opc == 1:
            t = input("nome da tarefa: ")
            print("Adicionando tarefa. . .")
            sleep(1)
            lista.append(t)
            print("Tarefa adicionada com sucesso!")
        elif opc == 2:
            remover = leiaInt('QUer remover qual tarefa? ')
            if remover < 0:
                print("Erro, digite um número positivo!")
                continue
            if 1 <= remover <= len(lista):
                print("Removendo tarefa . . .")
                sleep(1)
                lista.pop(remover-1)
                print("Tarefa removida com sucesso!")
            else:
                print("Não há tarefas para remover!")
        elif opc == 3:
            listar_tarefas(lista)
        elif opc ==4:
            cabecalho("Encerrando o programa . . .")
            sleep(1)
            break
        else:
            print("Valor inválido! ")
    salvar(lista)
    print(" Arquivo Salvo com sucesso!")
    sleep(1)



main()


