def menu():
    print('='*30)
    print('Menu'.center(30))
    print('=' * 30)
    print('[1] - Acessar conta')
    print('[2] - Criar cadastro')
    print('[3] - Sair')

def criacadastro():
    print('=' * 30)
    print('Cadastro de usuário'.center(30))
    print('=' * 30)
    while True:
        nome = str(input('Digite um nome: '))
        if nome in usuarios:
            print('')
            print('Esse nome já foi cadastrado! Tente um nome diferente.')
            print('')
        elif nome.isspace():
            print('')
            print('Espaço vazio não vale! :/')
            print('')
        else:
            print('')
            print('Gostei desse nome :B')
            break
    print('Agora vamos cadastrar sua senha! ')
    while True:
        senha = str(input('Digite uma senha: '))
        if senha.isspace():
            print('')
            print('Espaço vazio não vale! :/')
            print('')
        else:
            break
    while True:
        senha2 = str(input('Digite novamente para confirmar: '))
        if senha == senha2:
            print('')
            print('Show! As senhas conferem! =D')
            print(f'Agora seu cadastro foi concluído! Seja muito bem vinda(o) {nome}')
            usuarios.append(nome)
            senhaLogin.append(senha)
            break
        else:
            print('')
            print('Poxa, as senhas não conferem :/')
            print('Vamos tentar novamente!')

def acessaconta():
    print('=' * 30)
    print('Login'.center(30))
    print('=' * 30)
    try:
        nome = str(input('Usuário: '))
        senha = str(input('Senha: '))
        p = usuarios.index(nome)
    except:
        if nome in usuarios:
            print('')
            print('Vish! Acho que você pode ter digitado errado alguma coisa.')
            print('Vamos tentar novamente ;)')
            acessaconta()
        else:
            print('')
            print('Parece que você ainda não tem cadastro!')
            print('Vamos retornar ao menu principal para que você possa criar um! :B')
            print('')
    else:
        if nome in usuarios and senha == senhaLogin[p]:
            print('')
            print('login realizado com sucesso!')
            print(f'Olá {nome}! Muito bom ver você por aqui! =D')
            menulog(nome)
        else:
            print('')
            print('Usuário ou senha incorretos :/.')

def menulog(nome):
    while True:
        print('')
        print('=' * 30)
        print(f'Menu da(o) {nome}'.center(30))
        print('=' * 30)
        print('[1] - Cadastrar nova senha')
        print('[2] - Apagar uma senha')
        print('[3] - Apagar todas as senhas')
        print('[4] - Ver lista de senhas')
        print('[5] - Apagar cadastro')
        print('[6] - Sair da conta')
        try:
            opc = int(input('=> '))
            while opc < 1 or opc > 6:
                print('')
                print('Lá vai uma dica... Tem que ser um número de 1 até 4 :P')
                menulog(nome)
                opc = int(input('=> '))
        except:
            print('')
            print('Colega, você tem que digitar um número :v')
        else:
            if opc == 1:
                cadastrasenha(nome)
            elif opc == 2:
                apagasenha(nome)
            elif opc == 3:
                apagatudo(nome)
            elif opc == 4:
                exibesenha(nome)
            elif opc == 5:
                apagacadastro(nome)
                if nome not in usuarios:
                    break
            elif opc == 6:
                break

def apagatudo(nome):
    print('')
    print('=' * 30)
    print(f'Gerenciador de senhas da {nome}'.center(30))
    print('Apagar todos os registros'.center(30))
    print('=' * 30)
    if nome not in gerenciador:
        print('')
        print('Você ainda não possui senhas cadastradas :(')
        menulog(nome)
    else:
        exibesenha(nome)
        print('')
        print('Vamos fazer aquela faxina!')
        try:
            print('Vamos apagar tudo mesmo? [S/N]')
            opc = str(input('=> ')).upper()
            while opc != 'S' and opc != 'N':
                print('Tem que ser "S" ou "N" :V')
                print('Vamos apagar tudo mesmo? [S/N]')
                opc = str(input('=> ')).upper()
        except:
            print('Vish! Vamos tentar de novo')
        else:
            gerenciador.pop(nome)
            print('Tudo apagado!')

def cadastrasenha(nome):
    print('')
    print('=' * 30)
    print('Gerenciador de senhas'.center(30))
    print(f'Cadastrar nova senha para {nome}'.center(30))
    print('=' * 30)
    identificador = []
    password = []
    if nome in gerenciador:
        base2 = []
        for i in range(len(gerenciador[nome][:])):
            base2.append(gerenciador[nome][i])
        gerenciador.pop(nome)
        print('')
        ids = str(input('Digite um identificador: '))
        passs = str(input('Digite a senha para guardar: '))
        base2.append(f'Nome: {ids} - Senha: {passs}')
        gerenciador[nome] = base2
    else:
        base = []
        print('')
        ids = str(input('Digite um identificador: '))
        passs = str(input('Digite a senha para guardar: '))
        base.append(f'Nome: {ids} - Senha: {passs}')
        gerenciador[nome] = base
        base = []

def apagasenha(nome):
    print('=' * 30)
    print('Gerenciador de senhas'.center(30))
    print('Apagar registro único'.center(30))
    print('=' * 30)
    if nome not in gerenciador:
        print('')
        print('Você ainda não possui senhas cadastradas :(')
        menulog(nome)
    else:
        exibesenha(nome)
        print('')
        print('Me mostra o ID da senha que você quer apagar que eu faço o resto ;)')
        try:
            opc = int(input('=> '))
        except:
            print('')
            print('Não encontrei esse ID, talvez você tenha digitado errado :V')
            print('Vamos tentar novamente')
            print('')
            apagasenha(nome)
        else:
            opc -= 1
            lista = []
            for i in range(len(gerenciador[nome][:])):
                lista.append(gerenciador[nome][i])
            gerenciador.pop(nome)
            del lista[opc]
            gerenciador[nome] = lista
            print('')
            print('Deleção realizada com sucesso!')
            print('')
            exibesenha(nome)

def apagacadastro(nome):
    print('=' * 30)
    print('Apagar cadastro'.center(30))
    print('=' * 30)
    print('Digite sua senha para confirmar.')
    print('')
    try:
        p = usuarios.index(nome)
        senha = str(input('Senha: '))
        while senha != senhaLogin[p]:
            print('Acho que você pode ter digitado errado, vamos tentar novamente.')
            senha = str(input('Senha: '))
        if nome in usuarios and senha == senhaLogin[p]:
            opc = str(input('Deseja realmente apagar o seu cadastro? [S/N]: ')).upper()
            while opc != 'S' and opc != 'N':
                print('Opção inválida. Pode ser um sinal para você não apagar sua conta! Pense bem :B')
                print('Vamos apagar tudo mesmo? [S/N]')
                opc = str(input('=> ')).upper()
    except:
        print('Acho que você pode ter digitado algo errado')
        print('Vamos tentar novamente')
        print('')
        apagacadastro(nome)
    else:
        if opc == 'S':
            print('Espero que nos encontremos novamente por esse mundo digital... ')
            if nome in gerenciador:
                gerenciador.pop(nome)
            del usuarios[p]
            del senhaLogin[p]
            print('Cadastro excluído! :(')
        else:
            print('Uhuuul! Eu sabia que ainda faríamos muitas senhas mirabolantes juntos! :D')

def exibesenha(nome):
    print('=' * 30)
    print(f'Senhas de {nome}'.center(30))
    print('=' * 30)
    lista = []
    if nome in gerenciador:
        lista.append(gerenciador[nome])
        for i in range(len(lista[0])):
            print(f'ID:[{i + 1}] | {lista[0][i]}')
    else:
        print('')
        print('Você ainda não possui senhas cadastradas :(')


usuarios = []
senhaLogin = []
gerenciador = {}

while True:
    menu()
    try:
        opc = int(input('=> '))
        while opc < 1 or opc > 3:
            print('Opção inválida! Tente novamente')
            menu()
            opc = int(input('=> '))
    except:
        print('opção inválida! Tente novamente.')
    else:
        if opc == 1:
            acessaconta()
        elif opc == 2:
            criacadastro()
        elif opc == 3:
            break
