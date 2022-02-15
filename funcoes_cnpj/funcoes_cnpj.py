from random import randint
def remove_caracteres(cnpj):
    cnpj=cnpj.replace('/','')
    cnpj=cnpj.replace('.','')
    cnpj=cnpj.replace('-','')
    return cnpj

def achar_primeiro_digito(cnpj):
    num_1=5
    num_2=9
    soma_total=0
    cnpj_modificado=list(cnpj)
    for pegar_digito in cnpj_modificado[0:4]:
        pegar_digito=int(pegar_digito)
        soma_total=(pegar_digito*num_1)+soma_total
        num_1-=1  
    for pegar_digito in cnpj_modificado[4:]:
        pegar_digito=int(pegar_digito)
        soma_total=(pegar_digito*num_2)+soma_total
        num_2-=1
    return soma_total

def conta_digitos(soma_total):
    conta=11-(soma_total%11)
    digito=conta if conta<=9 else 0
    digito=str(digito)
    return digito

def achar_segundo_digito(cnpj_com_primeiro_digito):
    num_1=6
    num_2=9
    soma_total=0
    cnpj_com_primeiro_digito=list(cnpj_com_primeiro_digito)
    for pegar_digito in cnpj_com_primeiro_digito[0:5]:
        pegar_digito=int(pegar_digito)
        soma_total=(pegar_digito*num_1)+soma_total
        num_1-=1
    for pegar_digito in cnpj_com_primeiro_digito[5:]:
        pegar_digito=int(pegar_digito)
        soma_total=(pegar_digito*num_2)+soma_total
        num_2-=1
    return soma_total

def gerar_cnpj():

    cnpj_8=randint(10000000,99999999)
    cnpj_especial='0001'
    cnpj_aleatorio=f'{cnpj_8}{cnpj_especial}'
    return cnpj_aleatorio



