produtos = []
def cadastrar_produto(produtos):
    nome = input('Digite o nome do produto: ')
    try:
        preço = float(input('Digite o preço do produto: R$'))
        quantidade = int(input('Quantidade do produto (0+): un '))
    except ValueError:
        print('Digite apenas números.')
        return 'cadastro_erro'
    if quantidade < 0:
        print('Digite apenas números igual ou maior que 0.')
        return
    produtos.append(
        {'Nome': nome, 'Preço': preço, 'Quantidade': quantidade}
    )
    print('Produto Adicionado.')

def listar_produtos(produtos):
    if not produtos:
        print('Nenhum produto encontrado.')
        return 'sem produtos'
    for i, produto in enumerate(produtos):
        print(f'ID[{i}] | [{produto['Nome'].capitalize()}] - R${produto['Preço']:.2f} por un - [{produto['Quantidade']} un]')

def atualizar_estoque(produtos):
    if listar_produtos(produtos) == 'sem produtos':
        return
    try:
        idx = int(input('Escolha o Id do produto que deseja modificar: '))    
    except ValueError:
        print('ID ou entrada inválida.')
        return
    if 0 > idx >= len(produtos):
        print('ID Inválido.')
        return
    escolha = int(input('1.Adcionar Unidades \n2.Remover Unidades \n3.Atualizar Quantidade \n4.Sair \nEscolha uma opção (1,2,3,4): '))
    if escolha not in [1,2,3,4]:
        print('Entrada Inválida.')
        return
    if escolha == 1:
        print(produtos[idx])
        try:
            aumento = int(input('Quantas unidades deseja aumentar? '))
        except ValueError:
            print('Use apenas números.')
            return
        if aumento >= 0:
            soma = aumento + produtos[idx]['Quantidade']
            produtos[idx]['Quantidade'] = soma
            print('Valor mudado com sucesso.')
            print(produtos[idx])
        else:
            print('Por favor, não use números negativos.')
            return
    elif escolha == 2:
        print(produtos[idx])
        try:
            remover = int(input('Quantas unidades deseja remover? '))
        except ValueError:
            print('Use apenas números')
            return
        if remover >= 0:
            menos = produtos[idx]['Quantidade'] - remover
            produtos[idx]['Quantidade'] = menos
            if produtos[idx]['Quantidade'] < 0:
                produtos [idx]['Quantidade'] = 0
            print('Valor mudado com sucesso.')
            print(produtos[idx])
        else:
            print('Por favor, não use números negativos.')
            return
    elif escolha == 3:
        print(produtos[idx])
        try:
            novo_valor = int(input('Digite o novo valor da unidade: '))
        except ValueError:
            print('Use apenas números.')
            return
        if novo_valor >= 0:
            produtos[idx]['Quantidade'] = novo_valor
            print('Valor mudado com sucesso.')
            print(produtos[idx])
        else:
            print('Por favor, não use números negativos.')
    elif escolha == 4:
        print('Encerrando...')
        return

def filtrar_estoque(produtos):
    if listar_produtos(produtos) == 'sem produtos':
        return
    try:
        limite = int(input('Digite o limite de estoque: '))
    except ValueError:
        print('Digite apenas números.')
        return
    filtradas = [p for p in produtos if p['Quantidade'] <= limite]
    listar_produtos(filtradas)

def valor_total(produtos):
    total = sum(p['Preço'] * p['Quantidade'] for p in produtos) 
    print(f'O valor total de todos os produtos é: {total:.2f}')

while True:
    print('\nSistema de Controle de Estoque   \n1- Cadastrar Produto  \n2- Listar os Produtos \n3- Atualizar Estoque  \n4- Filtrar Produtos com o Estoque Abaixo de um Limite.    \n5- Sair do Programa. \n6- Valor total dos produtos \n')
    try:
        opçao = int(input('Selecione uma das opções (1,2,3,4,5): '))
    except ValueError:
        print('Entrada Inválida.')
        continue
    if opçao == 1:
        cadastrar_produto(produtos)
    elif opçao == 2:
        listar_produtos(produtos)
    elif opçao == 3:
        atualizar_estoque(produtos)
    elif opçao == 4:
        filtrar_estoque(produtos)
    elif opçao == 5:
        print('Encerrando...')
        break
    elif opçao == 6:
        valor_total(produtos)
    else:
        print('Entrada Inválida.')
        continue