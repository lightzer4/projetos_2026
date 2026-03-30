#Crie uma função onde recebe o nome aluno e a nota do aluno (nota deve ser float), o nome do aluno não deve ser vazio/null.
# #O Aluno deve receber 3 notas e a função deve calcular a média.

def aluno(nome, nota1, nota2, nota3):
    if nome == '':
        print('nome nao deve ser vazio')
        return
    media = (nota1 + nota2 + nota3) / 3
    print('media:', media)
    if nota1 > 10 or nota2 > 10 or nota3 > 10:
        print('nota deve ser menor que 10')

x = input('digite seu nome: ')
y = float(input('sua primeira nota: '))
z = float(input('sua segunda nota: '))
j = float(input('sua terceira nota: '))

aluno(x, y, z, j)
