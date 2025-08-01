def notas(*numeros, sit=False):
    maior = max(numeros)
    total = sum(numeros)
    menor = min(numeros)
    media = sum(numeros)/len(numeros)
    dicio = {'Total': total, 'Maior': maior, 'Menor': menor, 'Média': media}
    if sit:
        if media < 4: 
            dicio['Situação']= 'Ruim'
        elif 7> media >= 4:
            dicio['Situação']= 'Razoável'
        else:
            dicio['Situação'] ='Boa'
    return dicio
resp = notas(3, 4, 6, 9, 10, sit=True)
print(resp)