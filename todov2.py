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














