from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda


print('\033[107;30;4mMercado feito por: Fernando de Souza Batista\033[40;97;0m')
print('\033[107;30;4mLinkedin: https://www.linkedin.com/in/fernando-batista-208048207/\033[40;97;0m')

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    print('====================================')
    print('=========== BEM-VINDO(A) ===========')
    print('===========  LOJA DO FSB ===========')
    print('====================================')

    print('Selecione uma opção abaixo: ')
    print('1 - Cadastrar produto')
    print('2 - Listar produtos')
    print('3 - Comprar produtos')
    print('4 - Visualizar carrinho')
    print('5 - Fechar pedido')
    print('6 - Sair do sistema')

    opcao: int = int(input())

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Volte sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida!')
        sleep(1)
        menu()


def cadastrar_produto() -> None:
    print('Cadastro de produto\n')

    nome: str = input('Informe o nome do produto: ')
    preco: float = float(input('Informe o preço do produto: '))

    produto: Produto = Produto(nome, preco)

    produtos.append(produto)

    print(f'O produto {produto.nome} foi cadastrado com sucesso!')
    sleep(1)
    menu()


def listar_produtos() -> None:
    if len(produtos) > 0:
        print('Listagem de produtos:\n')
        for produto in produtos:
            print(produto)
            print('-------------')
            sleep(1)

    else:
        print('Não à nenhum produto cadastrado.')
    sleep(2)
    menu()


def comprar_produto() -> None:
    if len(produtos) > 0:  # Verifica se há produto cadastrado.
        print('Informe o código do produto que deseja adicionar ao carrinho:\n')
        print('Produtos disponíveis:')
        for produto in produtos:
            print(produto)
            print('----------------------')
            sleep(1)
        codigo: int = int(input())

        produto: Produto = pega_produto_por_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quantidade: int = item.get(produto)
                    if quantidade:
                        item[produto] = quantidade + 1
                        print(f'O produto {produto.nome} possui {quantidade + 1} unidades no carrinho.')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionado no carrinho.')
                    sleep(2)
                    menu()
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado com sucesso!')
                sleep(2)
                menu()
        else:
            print(f'O produto com código: {codigo} não foi encontrado.')
            sleep(2)
            menu()

    else:
        print('Ainda não há produto à venda.')
    sleep(2)
    menu()


def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos no carrinho: ')

        for item in carrinho:
            for dados in item.items():
                print(dados[0])  # Produto
                print(f'Quantidade: {dados[1]}\n')  # Quantidade
                sleep(1)
    else:
        print('Não à nenhum produto no carrinho.')
    sleep(2)
    menu()


def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print('Produtos do carrinho:')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += valor_total + dados[0].preco * dados[1]  # Soma o produto e a quantidade dele no carrinho
                print('----------------')
                sleep(1)
        print(f'Sua fatura é {formata_float_str_moeda(valor_total)}')
        print('Volte sempre!')
        carrinho.clear()
        sleep(5)
    else:
        print('Não à nenhum produto no carrinho.')
        sleep(2)
        menu()


def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto

    return p


if __name__ == '__main__':
    main()
