def vote(nascimento):
    from datetime import date
    ano_atual = date.today().year
    idade_atual = ano_atual - nascimento
    if idade_atual < 16:
        return f'Com {idade_atual}: Não vota'
    elif 16 <= idade_atual < 18 or idade_atual > 70:
        return f'Com {idade_atual}: Voto opcional'
    else:
        return f'Com {idade_atual}: Voto obrigatório'

nascimento = int(input('Digite o ano de nascimento: '))
print(vote(nascimento))