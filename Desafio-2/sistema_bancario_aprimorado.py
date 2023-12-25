LIMITE_SAQUE = 500
QT_MAX_SAQUES = 2
AGENCIA = "0001"
saques_feitos,deposito,saque,saldo,n_conta = 0,0,0,0,0
registro_clientes,registro_contas,registro_depositos,registro_saques = [],[],[],[]




def saque(*,valor_saque):
    global LIMITE_SAQUE
    global QT_MAX_SAQUES
    global saques_feitos
    global registro_saques
    global saldo

    if saques_feitos <= QT_MAX_SAQUES:
            if valor_saque <= LIMITE_SAQUE:
                if valor_saque <= saldo:
                    print("Dinheiro sacado com sucesso.")
                    registro_saques.append(f"R$ {valor_saque: .2f}")
                    saldo -= valor_saque
                    saques_feitos += 1
                else:
                    print(""" 
                    Saldo insuficiente, verifique seu saldo e tente novamente.
                     """)
            else:
                print(f"Limite de valor a ser sacado excedido, máximo R${LIMITE_SAQUE: .2f}")
    else:
        print(""" 
        Limite de saque excedido, maximo 3 por sessão.
         \n""")

def deposito(valor_deposito):
    global registro_depositos
    global saldo

    if valor_deposito == 0:
        print("Não foi depositado nenhum valor.")

    registro_depositos.append(f"R$ {valor_deposito: .2f}")
    saldo += valor_deposito

    print(f"""
            Foram depositados: R${valor_deposito: .2f}
            Saldo atual: R${saldo: .2f}
            """)

def extrato(saldo,*,registro_depositos,registro_saques):
    if not registro_depositos:
            registro_depositos.append("Não existem depositos registrados.")
    if not registro_saques:
        registro_saques.append("Não existem saques registrados.")
    
    print(f"Depositos :\n *{'\n *'.join(registro_depositos)}\n")
    print(f"Saques :\n *{'\n *'.join(registro_saques)}\n")
    print(f"Saldo Atual : R$ {saldo: .2f}")

def cadastrar_cliente(cliente):
    global registro_clientes
    if all(cliente.values()):
        print("Registro válido, continuando registro...")
    else:
        print("\nCampo vázio. Por favor preencha todos os campos.")
        return
    registro_clientes.append(cliente)
    print(f"Cliente {cliente["nome"]} foi registrado com sucesso, agora siga para a opção de cadastrar conta usando o CPF do cliente.")

    print("Cadastrado com Sucesso!")

def cadastrar_conta_bancaria(agencia,n_conta,cpf_cliente):
    global registro_clientes
    global registro_contas
    cpfs_validos = [clientes['cpf'] for clientes in registro_clientes if 'cpf' in clientes]
    if cpf_cliente in cpfs_validos:
        print("Cliente encontrado, criando conta!")
        n_conta += 1
        conta = {'agencia': agencia,'n_conta': n_conta,'cliente': cpf_cliente}
        registro_contas.append(conta)
    else:
        print("Cliente não encontado.")

def acessar_cliente(cpf_cliente):
    global registro_clientes
    global registro_contas
    
    cliente_selecionado = ""
    print(registro_clientes)
    for cliente in registro_clientes:
        print(cliente['cpf'])
        if cpf_cliente in cliente['cpf']:
            cliente_selecionado = cliente
        else:
            print("Cliente ainda não tem registro.")
            break

    return cliente_selecionado



while True:
    menu = int(input(f"""
    Bem vindo ao Banco Popular, digite uma opção para continuar:
    \n
    [1] Acessar Conta
    [2] Criar Cliente
    [3] Criar Conta
    [0] Sair
    \n\n"""))

    if menu== 1:
        cliente_selecionado = acessar_cliente(input("Digite o CPF do cliente: "))
        print(cliente_selecionado)
        if cliente_selecionado:
            while True:
                menu2 = int(input(f"""
                Bem vindo ´{cliente_selecionado['nome']}, digite uma opção para continuar:
                \n
                [1] Saque
                [2] Deposito
                [3] Extrato
                [0] Sair
                \n
                Saldo Atual : R$ {saldo: .2f}\n\n"""))
                    
                if menu2 == 1:
                    saque(valor_saque = int(input("""
                                    Saque limitado a até R$500 por vez.
                                    Digite o valor para saque: 
                                    """)))
                    
                    
                elif menu2 == 2:
                    deposito(int(input("Digite o valor a ser depositado: ")))

                elif menu2 == 3:
                    extrato(saldo,registro_depositos = registro_depositos, registro_saques = registro_saques)      

                elif menu2 == 0:
                    break

                else:
                    print("Opção não identificada, tente novamente.")
        else:
            print("Usuario não encontador.")

    elif menu == 2:
        nome = input("Digite o nome do cliente: ")
        data_nascimento = input("Digite a data de nascimento do cliente: ")
        cpf = input("Digite apenas os numeros do CPF do cliente: ")
        print("\nDigite agora o endereço do cliente: \n")
        logradouro = input("Digite o logradouro do cliente: ")
        numero = input("Digite o numero da casa/apartamento do cliente: ")
        bairro = input("Digite o nome do bairro do cliente: ")
        cidade_uf = input("Digite o nome da cidade e UF do cliente: (Exemplo : Cuiabá/MT) ")
        cliente = {'nome': nome,'data_nascimento': data_nascimento,'cpf': cpf,'endereco': {'logradouro': logradouro,'numero': numero,'bairro': bairro,'cidade_uf': cidade_uf}}
        cadastrar_cliente(cliente)
        print(registro_clientes)
    
    elif menu == 3:
        cpf_cliente = input("Digite o número do CPF do Cliente que deseja cadastrar nova conta : \n")
        cadastrar_conta_bancaria(AGENCIA,n_conta,cpf_cliente)

    elif menu == 0:
        break
    else:
        print("Opção não identificada, tente novamente.")

    



