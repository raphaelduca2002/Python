"""6.	Conforme a tabela abaixo, desenvolva um algoritmo que leia um código do produto informado pelo usuário e
informe a descrição do lanche.

CÓDIGO	DESCRIÇÃO DO PRODUTO
100		X-Salada com coca-cola.
200		Hot dog com suco de laranja
300		Sanduíche natural com suco de uva.
400		Misto Quente com fanta laranja.
500		Pão com manteiga com café.
600		Pão com manteiga na chapa com café com leite.
		Qualquer outro código diferente dos códigos da tabela, informar a mensagem Código informado inválido."""

codigo = int(input("Informe o código do lanche (100,200,300,400,500,600): "))

lanche100 = "X-Salada com coca-cola."
lanche200 = "Hot dog com suco de Laranja."
lanche300 = "Sanduíche natural com suco de uva"
lanche400 = "Misto Quente com fanta laranja."
lanche500 = "Pão com manteiga com café."
lanche600 = "Pão com manteiga na chapa com café com leite."

match codigo:
    case 100:
        print(lanche100)
    case 200:
        print(lanche200)
    case 300:
        print(lanche300)
    case 400:
        print(lanche400)
    case 500:
        print(lanche500)
    case 600:
        print(lanche600)
    case _:
        print("Código informado Inválido!")
