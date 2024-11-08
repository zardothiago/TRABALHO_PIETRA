hospede_1, hospede_2, hospede_3, hospede_4, hospede_5 = "", "", "", "", ""
entrada_1, entrada_2, entrada_3, entrada_4, entrada_5 = "", "", "", "", ""
saida_1, saida_2, saida_3, saida_4, saida_5 = "", "", "", "", ""
quarto_1, quarto_2, quarto_3, quarto_4, quarto_5 = 0, 0, 0, 0, 0

cont = 1
while cont > 0: 

    print("SEJA BEM-VINDO(A) AO HOTEL")
    print("-- MENU --\n1 - CADASTRO\n2 - CONSULTA DE QUARTOS DISPONÍVEIS\n3 - REGISTRO ENTRADA E SAÍDA\n4 - HÓSPEDES CADASTRADOS\n5 - SAIR")
    opcoes_1 = int(input("QUAL OPÇÃO VOCÊ DESEJA ACESSAR: "))
    match (opcoes_1):
        case 1:
            cont_1 = 0
            while cont_1 == 0:
                if quarto_1 == 0:
                    print("-- CADASTRO DE HÓSPEDES --")
                    hospede_1 = input("ESCREVA O NOME DO HÓSPEDE: ")
                    print("VOCÊ ESTÁ NO QUARTO 01")
                    entrada_1 = (input("DATA DE ENTRADA: "))
                    saída_1 = (input("DATA DE SAÍDA: "))
                    quarto_1 = 1
                    cont_1 = 1
                    break
                if quarto_2 == 0:
                    print("-- CADASTRO DE HÓSPEDES --")
                    hospede_2 = input("ESCREVA O NOME DO HÓSPEDE: ")
                    print("VOCÊ ESTÁ NO QUARTO 02")
                    entrada_2 = (input("DATA DE ENTRADA: "))
                    saída_2 = (input("DATA DE SAÍDA: "))
                    quarto_2 = 1
                    cont_1 = 1
                    break
                if quarto_3 == 0:
                    print("-- CADASTRO DE HÓSPEDES --")
                    hospede_3 = input("ESCREVA O NOME DO HÓSPEDE: ")
                    print("VOCÊ ESTÁ NO QUARTO 03")
                    entrada_3 = (input("DATA DE ENTRADA: "))
                    saída_3 = (input("DATA DE SAÍDA: "))
                    quarto_3 = 1
                    cont_1 = 1
                    break
                if quarto_4 == 0:
                    print("-- CADASTRO DE HÓSPEDES --")
                    hospede_4 = input("ESCREVA O NOME DO HÓSPEDE: ")
                    print("VOCÊ ESTÁ NO QUARTO 04")
                    entrada_4 = (input("DATA DE ENTRADA: "))
                    saída_4 = (input("DATA DE SAÍDA: "))
                    quarto_4 = 1
                    cont_1 = 1
                    break
                if quarto_5 == 0:
                    print("-- CADASTRO DE HÓSPEDES --")
                    hospede_5 = input("ESCREVA O NOME DO HÓSPEDE: ")
                    print("VOCÊ ESTÁ NO QUARTO 05")
                    entrada_5 = (input("DATA DE ENTRADA: "))
                    saída_5 = (input("DATA DE SAÍDA: "))
                    quarto_5 = 1
                    cont_1 = 1
                    break

        case 2:
            print("-- QUARTOS DISPONÍVEIS --")
            if len(quarto_1) > 0:
                if quarto_1 == 0:
                    print("QUARTO 01")
                if quarto_2 == 0:
                    print("QUARTO 02")
                if quarto_3 == 0:
                    print("QUARTO 03")
                if quarto_4 == 0:
                    print("QUARTO 04")
                if quarto_5 == 0:
                    print("QUARTO 05")
                if quarto_1 == 1 and quarto_2 == 1 and quarto_3 == 1 and quarto_4 == 1 and quarto_5 == 1:
                    print("NENHUM QUARTO DISPONÍVEL NO MOMENTO!")
            else:
                print("NENHUM HOSPEDE CADASTRADO!")

        case 3:
            print("-- REGISTRO ENTRADA E SAÍDA --")
            if len(hospede_1) > 0:
                print(f"QUARTO 01 - ENTRADA:{entrada_1} / SAÍDA:{saida_1}")
            if len(hospede_2) > 0:
                print(f"QUARTO 02 - ENTRADA:{entrada_2} / SAÍDA:{saida_2}")
            if len(hospede_3) > 0:
                print(f"QUARTO 03 - ENTRADA:{entrada_3} / SAÍDA:{saida_3}")
            if len(hospede_4) > 0:
                print(f"QUARTO 04 - ENTRADA:{entrada_4} / SAÍDA:{saida_4}")
            if len(hospede_5) > 0:
                print(f"QUARTO 05 - ENTRADA:{entrada_5} / SAÍDA:{saida_5}")
    
            cont_1 = 1
            while cont_1 > 0:
                print("-- MENU --\n1 - ATUALIZAR DATA DE SAÍDA\n2 - CHECK-OUT\n0 - SAIR")
                opcoes_2 = int(input("QUAL OPÇÃO VOCÊ DESEJA ACESSAR: "))
                match (opcoes_2):
                    case 1:
                        print("-- ATUALIZAR DATA DE SAÍDA --")
                        if len(hospede_1) > 0:
                            opcoes_3 = int(input("QUAL QUARTO VOCÊ DESEJA ATUALIZA: "))
                            match (opcoes_3):
                                case 1:
                                    if quarto_1 == 1:
                                        nova_saida_1 = input("DATA DE SAÍDA: ")
                                        saida_1 = nova_saida_1
                                case 2:
                                    if quarto_2 == 1:
                                        nova_saida_2 = input("DATA DE SAÍDA: ")
                                        saida_2 = nova_saida_2
                                case 3:
                                    if quarto_3 == 1:
                                        nova_saida_3 = input("DATA DE SAÍDA: ")
                                        saida_3 = nova_saida_3
                                case 4:
                                    if quarto_4 == 1:
                                        nova_saida_4 = input("DATA DE SAÍDA: ")
                                        saida_4 = nova_saida_4
                                case 5:
                                    if quarto_5 == 1:
                                        nova_saida_5 = input("DATA DE SAÍDA: ")
                                        saida_5 = nova_saida_5
                                case _:
                                    print("OPÇÃO INVÁLIDA!")
                        else:
                            print("NENHUM HÓSPEDE CADASTRADO!")
                    case 2:
                        print("-- CHECK-OUT --")
                        if len(hospede_1) > 0:
                            opcoes_3 = int(input("QUAL QUARTO VOCÊ DESEJA REALIZAR CHECH-OUT: "))
                            match (opcoes_3):
                                case 1:
                                    if quarto_1 == 1:
                                        quarto_1 = 0
                                        print("VOCÊ DESOCUPOU O QUARTO 01")
                                    else:
                                        print("QUARTO NÃO OCUPADO!")
                                case 2:
                                    if quarto_2 == 1:
                                        quarto_2 = 0
                                        print("VOCÊ DESOCUPOU O QUARTO 02")
                                    else:
                                        print("QUARTO NÃO OCUPADO!")
                                case 3:
                                    if quarto_3 == 1:
                                        quarto_3 = 0
                                        print("VOCÊ DESOCUPOU O QUARTO 03")
                                    else:
                                        print("QUARTO NÃO OCUPADO!")
                                case 4:
                                    if quarto_4 == 1:
                                        quarto_4 = 0
                                        print("VOCÊ DESOCUPOU O QUARTO 04")
                                    else:
                                        print("QUARTO NÃO OCUPADO!")
                                case 5:
                                    if quarto_5 == 1:
                                        quarto_5 = 0
                                        print("VOCÊ DESOCUPOU O QUARTO 05")
                                    else:
                                        print("QUARTO NÃO OCUPADO!")
                                case _:
                                    print("OPÇÃO INVÁLIDA!")
                        else:
                            print("NENHUM HÓSPEDE CADASTRADO!")
                    case 0:
                        cont_1 = 0
                    case _:
                        print("OPÇÃO INVÁLIDA!")
        
        case 4:
            if quarto_1 == 1:
                print(f"NOME: {hospede_1} \nQUARTO: 01 \nENTRADA: {entrada_1} \nSAÍDA: {saida_1}")
            if quarto_2 == 1:
                print(f"NOME: {hospede_2} \nQUARTO: 02 \nENTRADA: {entrada_2} \nSAÍDA: {saida_2}")
            if quarto_3 == 1:
                print(f"NOME: {hospede_3} \nQUARTO: 03 \nENTRADA: {entrada_3} \nSAÍDA: {saida_3}")
            if quarto_4 == 1:
                print(f"NOME: {hospede_4} \nQUARTO: 04 \nENTRADA: {entrada_4} \nSAÍDA: {saida_4}")
            if quarto_5 == 1:
                print(f"NOME: {hospede_5} \nQUARTO: 05 \nENTRADA: {entrada_5} \nSAÍDA: {saida_5}")
            else:
                print("NENHUM HÓSPEDE CADASTRADO!")
        case _:
                print("OPÇÃO INVÁLIDA!")