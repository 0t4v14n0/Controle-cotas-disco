#////////////////////SOMA///////////////////////////////////
def calculos(ordenação):
    soma = 0
    for linha in ordenação:
        numero = int(linha[1])
        linha[1] = numero
        soma += numero
    return soma

#///////////////////ORDENAÇÃO/////////////////////////////
def ordena(segura,ordena_segura):
    ordena_segura = sorted(segura, key = lambda x: x[1])
    return ordena_segura

#///////////////////MONTAR ARQUIVO FINAL///////////////////
def montar_arq(ordenação,soma):
    with open('relatório.txt','w') as arquivofinal:
        arquivofinal.write('ACME Inc.\t\tUso do espaço em disco pelos usuários \n')
        arquivofinal.write('------------------------------------------------------------------------\n')
        arquivofinal.write('Nr.  Usuário\t\tEspaço utilizado\t\t% do uso\n')
        contador = 0
        media = 0
        for linha in ordenação:
            contador = contador + 1
            porc = ((linha[1]/soma)*100)
            arquivofinal.write(f'{contador}  {linha[0]}\t\t{round(linha[1],2)} MB\t\t\t{round(porc,2)}%\n')
            #linha_formatada = '\t'.join(map(str, linha)) + '\n'
            #arquivofinal.write(linha_formatada)
        arquivofinal.write('\n')
        arquivofinal.write(f'Espaço total ocupado: {round(soma,2)} MB \n')
        media = int (soma)/contador
        arquivofinal.write(f'Espaço médio ocupado: {round(media,2)} MB \n')

#abri o arquivo usuarios, FOR passa linha por linha do arquivo e mostra no terminal com o print

def usuario(segura):
    with open('usuarios.txt', 'r') as arquivo:

        for linha in arquivo:
            colunas = linha.split()
            nome, mb = colunas
            arrayse = [nome , mb]
            segura.append(arrayse)

#//////////////////////INICIO/////////////////////////

segura = []
ordena_segura = []

usuario(segura)

ordenação = ordena(segura,ordena_segura)

soma = calculos(ordenação)

montar_arq(ordenação, soma)