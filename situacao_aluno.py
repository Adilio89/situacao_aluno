"""
REFEITO PROGRAMA QUE CALCULA A MÉDIA DO ALUNO DO LIVRO PYTHON SEM MISTÉRIOS

CRIE UM PROGRAMA QUE SOLICITA AO USUÁRIO O NOME DE UM ALUNO E UMA NOTA, 
ARMAZENANDO ESSAS INFORMAÇÕES EM SEGUIDA E PERGUNTANDO SE O USUARIO DESEJA
INFORMAR A NOTA DE MAIS ALGUM ALUNO; EM CASO POSITIVO, REPITA A OPERAÇÃO 
PARA O PROXIMO ALUNO E CONTINUE A FAZÊ-LO ATÉ QUE O USUÁRIO ESCOLHA NÃO 
CONTINUAR. QUANDO ISSO OCORRER, IMPRIMA A LISTAGEM DOS ALUNOS, DE MODO QUE
CADA LINHA EXIBA: NOME DO ALUNO, TODAS AS SUAS NOTAS, A MÉDIA DELE E, CASO ESSA
MÉDIA SEJA MAIOR OU IGUAL 7.0 A PALAVRA "APROVADO"; SE A MÉDIA FOR MENOR 
QUE 7.0 E MAIOR OU IGUAL A 3.0, "FARÁ A PROVA FINAL"; E CASO NÃO FIQUE EM NENHUM
DESSES INTERVALOS, "REPROVADO".
"""

alunos = []
total_individual = 0.0
continua_loop_alunos = 'S'
continua_cadastro_notas = 'S'

while continua_loop_alunos == 'S':
    registro_aluno = {
        'nome': '',
        'notas' : [],
        'media' : 0.0
    }
    
    nome = input('Entre com o nome do aluno: ')
    registro_aluno['nome'] = nome
    indice = 0
    total_individual = 0

    while continua_cadastro_notas == 'S':
        indice = indice + 1
        print('Digite a nota n. %d: ' % indice)
        nota = float(input())
        registro_aluno['notas'].append(nota)
        total_individual = total_individual + nota
        print('Deseja Cadastrar Outra Nota ? [S-continua/N-encerrar estapa]')
        continua_cadastro_notas = str.capitalize(input())
        
    registro_aluno['media'] = total_individual / len(registro_aluno['notas'])
    alunos.append({'aluno': registro_aluno})
    print('Deseja Cadastrar as Notas de outro Aluno ? [S-continua/N-proximo aluno]')
    continua_loop_alunos = str.capitalize(input())
    continua_cadastro_notas = 'S'
    
for registro in alunos:
    if registro['aluno']['media'] >= 7.0:
        print(f'Nome: {registro["aluno"]["nome"]} - Notas: {registro["aluno"]["notas"]} - Média: {registro["aluno"]["media"]} - APROVADO')
    elif registro['aluno']['media'] >= 3.0:
        print(f'Nome: {registro["aluno"]["nome"]} - Notas: {registro["aluno"]["notas"]} - Média: {registro["aluno"]["media"]} - FARÁ PROVA FINAL')
    else:
        print(f'Nome: {registro["aluno"]["nome"]} - Notas: {registro["aluno"]["notas"]} - Média: {registro["aluno"]["media"]} - REPROVADO')    
