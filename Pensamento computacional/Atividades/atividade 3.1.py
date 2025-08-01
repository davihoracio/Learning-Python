alturainiciallevi = float(input('Altura inicial de Levi: '))
crescimentolevi = float(input('Taxa de crescimento de Levi: '))

alturainicialhiago = float(input('Altura inicial de Hiago: '))
crescimentohiago = float(input('Taxa de crescimento de Hiago: '))

if alturainiciallevi >= alturainicialhiago:
    print('Erro: Hiago deve ser maior que Levi inicialmente.')
elif crescimentohiago >= crescimentolevi:
    print('Erro: A taxa de crescimento de Levi deve ser maior que a de Hiago.')
else:
    anos = 0
    cresclevi = crescimentolevi / 100
    creschiago = crescimentohiago / 100
    while alturainiciallevi <= alturainicialhiago:
        alturainiciallevi += cresclevi
        alturainicialhiago += creschiago
        anos += 1
    print('Serão necessários {} anos para que Levi seja maior que Hiago.'.format(anos))
