from funcoes_cnpj.funcoes_cnpj import*
while True:
    print(80*'#')
    print('\t\t\tVALIDADOR/GERADOR DE CNPJ')
    print(80*'#')
    op=input('[1] - Validar CNPJ\n[2] - Gerar CNPJ\n[3] - Sair\nEscolha a opção: ')
    if not op=='1'and not op =='2'and not op=='3':
        print('Digite uma opção válida!!')
        continue
    if op=='1':
        cnpj_digitado=input('Digite um CNPJ para ser validado (00.000.000/0000-00): ')
        cnpj_so_numeros=remove_caracteres(cnpj_digitado) 
        if cnpj_so_numeros[0]*len(cnpj_so_numeros)==cnpj_so_numeros: #verifica se o CNPJ digitado é uma sequencia
            print('Digite um CNPJ válido!!')
            continue
        if not cnpj_so_numeros.isnumeric() or len(cnpj_so_numeros)<14:
            print('Digite um CNPJ válido!!')
            continue
        p1=achar_primeiro_digito(cnpj_so_numeros[0:12])
        conta=conta_digitos(p1)
        cnpj_1=cnpj_so_numeros[0:12]+conta
        p2=achar_segundo_digito(cnpj_1)
        cnpj_2=conta_digitos(p2)
        cnpj_f=cnpj_1+cnpj_2
        cnpj_f=f'{cnpj_f[0:2]}.{cnpj_f[2:5]}.{cnpj_f[5:8]}/{cnpj_f[8:12]}-{cnpj_f[12:]}'

        if cnpj_digitado==cnpj_f:
            print(f'O CNPJ {cnpj_digitado} é válido!!!')
        else:
            print(f'O CNPJ {cnpj_digitado} é invalido!!!')
    elif op=='2':
        cnpj_ale=gerar_cnpj()
        p1=achar_primeiro_digito(cnpj_ale)
        conta=conta_digitos(p1)
        cnpj_1=cnpj_ale+conta
        p2=achar_segundo_digito(cnpj_1)
        cnpj_2=conta_digitos(p2)
        cnpj_f=cnpj_1+cnpj_2
        cnpj_f=f'{cnpj_f[0:2]}.{cnpj_f[2:5]}.{cnpj_f[5:8]}/{cnpj_f[8:12]}-{cnpj_f[12:]}'
        print(f'O CNPJ gerado foi {cnpj_f}')
    else:
        break
    sair=input('Deseja sair s/n? ')
    if sair=='s':
        break

