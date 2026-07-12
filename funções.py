def linha(tam=35):
    return print('-'*tam)


def cabeçalho(txt):
    linha()
    print(txt.center(35))
    linha()
    

def menu(lista):
    c=1
    for item in lista:
        print(f'{c} - {item}')
        c+=1
    linha()
    opc = leiaInt('Escolha uma opção: ')
    return opc


def leiaInt(msg):
    while True:
        try:
            resp = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
        else:
            if resp < 7 and resp > 0:
                return resp
            else:
                print('\033[31mERRO: por favor, digite uma opção válida.\033[m')