def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while (x < min) or (x > max):
        x = int(input(pergunta))
    return x

def criaArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Error na criação do arquivo') #ERROR genérico
    else:
        print('Arquivo {} foi criado com sucesso!\n'.format(nomeArquivo))

def existe_arquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def listar_arquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'r')
    except:
        print('Error ao ler o arquivo')
    else:
        print(a.read())
    finally:
        a.close()

def cadastrar_jogo(nomeArquivo, nome_jogo, nome_videogame):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('ERROR ao abrir o arquivo')
    else:
        a.write('{};{}\n'.format(nome_jogo,nome_videogame))
    finally:
        a.close()

# Programa principal
arquivo = 'games.txt'
if existe_arquivo(arquivo):
    print('Arquivo localizado no computador')
else:
    print('Arquivo inexistente')
    criaArquivo(arquivo)

while True:
    print('MENU')
    print('1 - Cadastrar novo item')
    print('2 - Listar cadastros')
    print('3 - Sair')

    op = valida_int('Escolha a opção desejada: ',1,3)
    if op == 1:
        print('Opção de cadastrar novo item selecionada...\n')
        nome_jogo = input('Nome do jogo:')
        nome_videogame = input('Nome do videogame:')
        cadastrar_jogo(arquivo, nome_jogo, nome_videogame)
    elif op == 2:
        print('Opção de listar selecionada...\n')
        listar_arquivo(arquivo)
    elif op == 3:
        print('Encerrando o programa...')
        break