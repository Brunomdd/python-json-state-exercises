# Enunciado: Sistema de Compra Simples
#
# Você deve desenvolver um programa em Python que simule um sistema de compras online
# com catálogo de produtos, carrinho de compras e finalização de compra.
#
# O programa deve ter as seguintes funcionalidades:
#
# 1️⃣ Catálogo de produtos
# - O sistema deve armazenar produtos em uma lista de dicionários.
# - Cada produto deve conter:
#     "nome" → nome do produto (string)
#     "preço" → preço do produto (float)
#     "estoque" → quantidade disponível no estoque (inteiro)
# Exemplo inicial:
# produtos = [
#     {"nome":"Iphone 15","preço":3913,"estoque":10},
#     {"nome":"Smart TV","preço":2550,"estoque":30},
# ]
#
# 2️⃣ Menu de opções
# O programa deve exibir um menu com as seguintes opções:
# - Catálogo → lista todos os produtos disponíveis com preço e estoque.
# - Adicionar ao carrinho → permite adicionar produtos ao carrinho, informando:
#     Nome do produto
#     Quantidade desejada
#     O sistema deve validar:
#       Nome válido
#       Quantidade não superior ao estoque
#     Se o produto já estiver no carrinho, a quantidade deve ser atualizada.
#     Mensagens de retorno:
#       "Produto adicionado ao carrinho com sucesso!"
#       "Quantidade maior que estoque"
#       "Produto não encontrado"
# - Ver carrinho → exibe todos os produtos adicionados ao carrinho com nome, quantidade e preço unitário.
# - Finalizar compra → calcula o total da compra, atualiza o estoque dos produtos e limpa o carrinho.
# - Sair do sistema → encerra o programa.
#
# 3️⃣ Validação de entradas
# - Todas as entradas numéricas devem ser validadas.
# - O programa deve ter uma função leiaInt() que garante que o usuário digite apenas números inteiros.
#
# 4️⃣ Observações
# - O carrinho é uma lista de dicionários contendo "nome", "quantidade" e "preço".
# - O estoque do produto deve ser atualizado apenas após a finalização da compra.
# - Se o carrinho estiver vazio e o usuário tentar ver ou finalizar a compra, o programa deve exibir mensagens informativas.


import json
from json import JSONDecodeError

def linha(l = 42):
    return "-" *l

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def carregar():
    """
    Carrega o catálogo de produtos a partir do arquivo 'ecommerce.json'.

    Tenta abrir e desserializar o arquivo JSON. Caso o arquivo não exista
    (FileNotFoundError) ou esteja corrompido/vazio (JSONDecodeError),
    retorna uma lista vazia para que o sistema use o catálogo padrão.

    :return: Lista de dicionários com os produtos salvos, ou lista vazia em caso de erro.
    """
    try:
        with open("ecommerce.json", "r", encoding="utf-8") as arq:
            return json.load(arq)
    except (FileNotFoundError, JSONDecodeError):
        return []


def salvar(produtos):
    """
    Salva o catálogo de produtos no arquivo 'ecommerce.json'.

    Serializa a lista de produtos em formato JSON com indentação de 4 espaços,
    garantindo a persistência do estoque atualizado entre execuções do programa.

    :param produtos: Lista de dicionários contendo os produtos com nome, preço e estoque.
    :return: None
    """
    with open("ecommerce.json", "w", encoding="utf-8") as arq:
        json.dump(produtos, arq, ensure_ascii=False, indent=4)


def leiaInt(num):
    """
    Solicita e valida uma entrada numérica inteira do usuário.

    Fica em loop até que o usuário digite um valor que possa ser convertido
    para inteiro. Exibe mensagem de erro caso a entrada seja inválida.

    :param num: String com a mensagem exibida ao usuário como prompt de entrada.
    :return: Valor inteiro digitado pelo usuário.
    """
    while True:
        try:
            valor = int(input(num))
            return valor
        except ValueError:
            print("Erro, digite um número válido!")


def listar_produtos(produtos):
    """
    Exibe no console todos os produtos disponíveis no catálogo.

    Para cada produto, imprime o nome, o preço e a quantidade em estoque.
    Não realiza nenhuma alteração nos dados.

    :param produtos: Lista de dicionários, cada um contendo 'nome', 'preço' e 'estoque'.
    :return: None
    """
    for p in produtos:
        print(f"Nome: {p['nome']} - Preço: {p['preço']} estoque:{p['estoque']}")


def adicionar_carrinho(produto, carrinho, nome, quantidade):
    """
    Adiciona um produto ao carrinho ou atualiza sua quantidade se já estiver presente.

    Percorre o catálogo em busca do produto pelo nome (case-insensitive).
    Valida se a quantidade solicitada está disponível no estoque.
    Se o produto já existir no carrinho, incrementa a quantidade;
    caso contrário, insere um novo item no carrinho.

    :param produto: Lista de produtos disponíveis no estoque (cada item é um dicionário com 'nome', 'preço' e 'estoque').
    :param carrinho: Lista de itens atualmente no carrinho.
    :param nome: Nome do produto que o usuário deseja adicionar.
    :param quantidade: Quantidade do produto a ser adicionada.
    :return: Retorna uma string indicando o resultado da operação:
             - "Sucesso" se o produto foi adicionado ou atualizado no carrinho.
             - "A Quantidade é maior que o estoque" se o estoque for insuficiente.
             - "Produto não encontrado" se o nome não existir no catálogo.
    """
    for p in produto:
        if p["nome"].lower() == nome.lower():
            if quantidade > p["estoque"]:
                return "A Quantidade é maior que o estoque"

            for item in carrinho:
                if item["nome"].lower() == nome.lower():
                    item["quantidade"] += quantidade
                    return "Sucesso"

            carrinho.append({"nome": nome, "quantidade": quantidade, "preço": p["preço"]})
            return "Sucesso"
    return "Produto não encontrado"


def ver_carrinho(carrinho):
    """
    Exibe no console todos os itens presentes no carrinho de compras.

    Caso o carrinho esteja vazio, informa o usuário e encerra a função.
    Para cada item, imprime o nome, a quantidade e o preço unitário.

    :param carrinho: Lista de dicionários contendo os itens no carrinho, com 'nome', 'quantidade' e 'preço'.
    :return: None
    """
    if not carrinho:
        print("não há produtos para mostrar")
        return

    for item in carrinho:
        print(f"produto: {item['nome']} - Quantidade: {item['quantidade']} Preço:{item['preço']}R$")


def finalizar_compra(carrinho, produtos):
    """
    Finaliza a compra, atualizando o estoque e calculando o valor total.

    Caso o carrinho esteja vazio, informa o usuário e retorna 0.
    Para cada item no carrinho, localiza o produto correspondente no catálogo,
    deduz a quantidade comprada do estoque e acumula o valor total da compra.
    Ao final, limpa o carrinho.

    :param carrinho: Lista de itens no carrinho, cada um com 'nome', 'quantidade' e 'preço'.
    :param produtos: Lista de produtos do catálogo, cada um com 'nome', 'preço' e 'estoque'.
    :return: Valor total (float) da compra finalizada, ou 0 se o carrinho estiver vazio.
    """
    if not carrinho:
        print("Adicione produtos no carrinho para finalizar a compra!")
        return 0

    total = 0
    for item in carrinho:
        item_nome = item["nome"]
        item_quantidade = item["quantidade"]
        for p in produtos:
            if p["nome"].lower() == item_nome.lower():
                p["estoque"] -= item_quantidade
                total += p["preço"] * item_quantidade

    carrinho.clear()
    return total

def main():
    cabecalho("Sistema de e-commerce")
    """
    Função principal do sistema de compras.

    Inicializa o catálogo carregando do arquivo JSON. Caso o arquivo não exista
    ou esteja vazio, utiliza um catálogo padrão hardcoded. Exibe um menu em loop
    até que o usuário escolha sair, momento em que o catálogo atualizado é salvo
    no arquivo JSON para persistência.

    :return: None
    """
    produtos = carregar()
    if not produtos:
        produtos = [
            {"nome": "Iphone 15",        "preço": 3913.00, "estoque": 10},
            {"nome": "Smart TV",         "preço": 2550.00, "estoque": 30},
            {"nome": "Notebook Dell",    "preço": 4200.00, "estoque": 15},
            {"nome": "Airpods Pro",      "preço": 1899.00, "estoque": 25},
            {"nome": "Mouse Logitech",   "preço": 299.00,  "estoque": 50},
            {"nome": "Teclado Mecânico", "preço": 450.00,  "estoque": 40},
            {"nome": "Monitor LG 24'",   "preço": 1200.00, "estoque": 20},
            {"nome": "SSD 1TB",          "preço": 380.00,  "estoque": 60},
            {"nome": "Headset Gamer",    "preço": 599.00,  "estoque": 35},
            {"nome": "Webcam Full HD",   "preço": 249.00,  "estoque": 45},
        ]
    carrinho = list()
    while True:
        print("1 - Catálago")
        print("2- Adicionar ao carrinho")
        print("3 - Ver carrinho")
        print("4 - Finalizar compra")
        print("5 - Sair do sistema")

        opc = leiaInt("Escolha uma opção: ")
        if opc == 1:
            listar_produtos(produtos)
        elif opc == 2:
            nome = str(input('nome: '))
            if not nome:
                print("digite um nome válido!")
                continue
            quantidade = leiaInt("quantidade: ")
            if quantidade <= 0:
                print("Erro quantidade invalida!")
                continue
            status = adicionar_carrinho(produtos, carrinho, nome, quantidade)
            if status == "Sucesso":
                print("Produto adicionado ao carrinho com sucesso!")
            elif status == "A Quantidade é maior que o estoque":
                print("Quantidade maior que estoque")
            else:
                print("Produto não encontrado")
        elif opc == 3:
            ver_carrinho(carrinho)
        elif opc == 4:
            finalizar = finalizar_compra(carrinho, produtos)
            print(f"O total da compra é {finalizar} R$")
        elif opc == 5:
            cabecalho("Saindo do sistema . . . ")
            break
    salvar(produtos)


main()
