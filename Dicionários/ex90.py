aluno = {}
aluno['Nome'] = input('Digite o nome do aluno: ')
aluno['Média'] = float(input(f'Digite a média do aluno {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5<= aluno['Média']< 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f'O {k} é {v}')