import hashlib

from Controller import ControllerCadastro, ControllerLogin

while True:
    print("======================================================================================")
    print("=                                       MENU                                         =")
    print("======================================================================================")
    print("= ESCOLHA UMA DAS OPÇÕES:                                                            =")
    print("======================================================================================")
    print("= 1 - CADASTRAR                                                                      =")    
    print("= 2 - LOGIN                                                                          =")    
    print("= 3 - SAIR                                                                           =")    
    print("======================================================================================")
    opcao = int(input("DIGITE: "))    

    if opcao == 1:
        nome = input("Digite o nome do usuário: ")
        email = input("Digite o e-mail: ")
        senha = input("Digite a senha: ")
        try:
            retorno_cadastro = ControllerCadastro.cadastrar(nome, email, senha)
            if retorno_cadastro == 1:
                print("Usuário cadastrado com sucesso.")
            elif retorno_cadastro == 2:
                print("Há problema com o nome, verifique os dados.")
            elif retorno_cadastro == 3:
                print("Há problema com o e-mail, verifique os dados.")
            elif retorno_cadastro == 4:
                print("Há problema com a senha, verifique os dados.")
            elif retorno_cadastro == 5:
                print("Já existe um usuário cadastrado com esse e-mail.")
            elif retorno_cadastro == 6:
                print("Erro interno o sistema. Dados não cadastrados.")

        except:
            print("Não foi possível realizar o cadastro.")

    if opcao == 2:
        print("======================================================================================")
        print("=                                    LOGIN                                           =")
        print("======================================================================================")
        email = input("DIGITE O E-MAIL: ")    
        senha = input("DIGITE A SENHA: ")    
        logado = ControllerLogin.login(email,senha)
        if logado:
            print("======================================================================================")
            print(f"USUÁRIO COM ID:{logado['id']} LOGADO. SEJA BEM VINDO!                  ")
            print("======================================================================================")

        else:
            print('DADOS INVÁLIDOS.')

    if opcao == 3:
        break