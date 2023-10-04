'''
Vamos supor que precisamos criar um programa para cadastrar
aluinos em uma escola, armazenando informações como nome,
idade e nota. A chave será o numero de matricula e o valor 
será outro dicionario contendo informações do aluno
'''
lista = {}
opcao = 1
while opcao !=3:
    print('='*10)
    print('==MENU==')
    print('1-Cadastrar aluno')
    print('2-CONSULTAR')
    print('3-SAIR')
    opcao = int(input('>>> '))
    if opcao ==1:
        matricula = input('Numero da matricula:')
        Nome = input('Nome do Aluno:')
        idade = input('Idade do aluno:')
        nota = input('Nota do aluno:')
        lista[matricula] = [Nome , idade , nota]
        print('adicionado com sucesso!!!')
    elif opcao ==2:
        MATRICULA = input('Codigo: ')
        if MATRICULA in lista:
            dados = lista[MATRICULA]
            print(f'Aluno:{dados}')
    elif opcao ==3:
        print('Saindo...')        
