from utils.helper import formata_float_str_moeda


class Produto:
    contador: int = 1

    def __init__(self: object, nome: str, preco: float) -> None:
        self.__codigo: int = Produto.contador
        self.__nome: str = nome
        self.__preco: float = preco
        Produto.contador += 1  # Incrementa o contador

    @property
    def codigo(self: object) -> int:
        return self.__codigo

    @property
    def nome(self: object) -> str:
        return self.__nome

    @ property
    def preco(self: object) -> float:
        return self.__preco

    def __str__(self: object) -> str:
        return f'Código: {self.codigo}\n' \
               f'Nome: {self.nome}\n' \
               f'Preço: {formata_float_str_moeda(self.preco)}\n'  # Preço do produto formatado
