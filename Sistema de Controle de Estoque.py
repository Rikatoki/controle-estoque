import system
produtos = []

while True:
    print('\nSistema de Controle de Estoque   \n1- Cadastrar Produto  \n2- Listar os Produtos \n3- Atualizar Estoque  \n4- Filtrar Produtos com o Estoque Abaixo de um Limite.    \n5- Sair do Programa. \n6- Valor total dos produtos \n')
    try:
        opçao = int(input('Selecione uma das opções (1,2,3,4,5): '))
    except ValueError:
        print('Entrada Inválida.')
        continue
    if opçao == 1:
        system.cadastrar_produto(produtos)
    elif opçao == 2:
        system.listar_produtos(produtos)
    elif opçao == 3:
        system.atualizar_estoque(produtos)
    elif opçao == 4:
        system.filtrar_estoque(produtos)
    elif opçao == 5:
        print('Encerrando...')
        break
    elif opçao == 6:
        system.valor_total(produtos)
    else:
        print('Entrada Inválida.')
        continue