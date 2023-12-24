LIMITE_SAQUE = 500
QT_MAX_SAQUES = 2
saques_feitos,deposito,saque,saldo = 0,0,0,0
registro_depositos,registro_saques=[],[]

while True:
    opcao = int(input("""
    Bem vindo ao Banco Popular, digite uma opção para continuar:
         \n
        [1] Saque
        [2] Deposito
        [3] Extrato
        [0] Sair
         \n"""))
    
    if opcao == 1:
        print(f"Saldo atual é R$ {saldo}")
        saque = int(input("""
                            Saque limitado a até R$500 por vez.
                            Digite o valor para saque: 
                            """))
        if saques_feitos <= QT_MAX_SAQUES:
            saques_feitos += 1
            if saque <= LIMITE_SAQUE:
                if saque <= saldo:
                    print("Dinheiro sacado com sucesso.")
                    registro_saques.append(f"R$ {saque: .2f}")
                    saldo -= saque
                else:
                    print("Saldo insuficiente, verifique seu saldo e tente novamente.")
        else:
            print("""\n \n Limite de saque excedido, maximo 3 por sessão.\n \n """)
        
    elif opcao == 2:
        print(f"Saldo atual é R$ {saldo}")
        deposito = int(input("Digite o valor a ser depositado: "))

        registro_depositos.append(f"R$ {deposito: .2f}")
        saldo += deposito

        print(f"""
                Foram depositados: R${deposito: .2f}
                Saldo atual: R${saldo: .2f}
                """)

    elif opcao == 3:
        if not registro_depositos:
            registro_depositos.append("Não existem depositos registrados.")
        if not registro_saques:
            registro_saques.append("Não existem saques registrados.")
        
        print(f"""
                Depositos :
                {' \n'.join(registro_depositos)}
                 \n
                "Saques :
                {' \n'.join(registro_saques)}
                 \n
                Saldo Atual : R$ {saldo: .2f}
                """)
            
    elif opcao == 0:
        break
    else:
        "Opção não identificada, tente novamente."