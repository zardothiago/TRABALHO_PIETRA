#DEFININDO VARIÁVEIS VAZIAS PARA GANHAR VALORES NO DECORRER DO CÓDIGO;
#ESSAS VARIÁVEIS SERÃO ESSENCIAIS PARA MOSTRAR A SITUAÇÃO DE CADASTRO DOS HÓSPEDES E TAMBÉM PARA AVISAR AO USUÁRIO CASO ELE ACESSE QUALQUER UMA DAS OPÇÕES DE PESQUISA ANTES DE FAZER O CADASTRO DE ALGUM HÓSPEDE;

hospede_1, hospede_2, hospede_3, hospede_4, hospede_5 = "", "", "", "", ""
entrada_1, entrada_2, entrada_3, entrada_4, entrada_5 = "", "", "", "", ""
saida_1, saida_2, saida_3, saida_4, saida_5 = "", "", "", "", ""
quarto_1, quarto_2, quarto_3, quarto_4, quarto_5 = 0, 0, 0, 0, 0

#INICIO O CÓDIGO COM UM LOOP PARA APARECER O MENU DE OPÇÕES ATÉ QUE O USUÁRIO ESCOLHA FINALIZAR AS OPERAÇÕES;

cont = 1
while cont > 0: 

    #MENU COM AS OPÇÕES DISPONÍVEIS PARA O USUÁRIO;

    print("SEJA BEM-VINDO(A) AO HOTEL")
    print("-- MENU --\n1 - CADASTRO\n2 - CONSULTA DE QUARTOS DISPONÍVEIS\n3 - REGISTRO ENTRADA E SAÍDA\n4 - HÓSPEDES CADASTRADOS\n0 - SAIR")
    opcoes_1 = int(input("QUAL OPÇÃO VOCÊ DESEJA ACESSAR: "))
    
    #USAREI A ESTRUTURA MATCH CASE PARA QUE O USUÁRIO ESCOLHA ENTRE AS OPÇÕES DISPONIVEIS OU PARA QUE O SISTEMA SE ENCERRE;
    #CASO O USUÁRIO ESCOLHA ALGUMA OPÇÃO QUE NÃO ESTEJA DISPONÍVEL ELE RECEBERÁ UMA MENSAGEM DE AVISO E O MENU TORNARÁ A APARECER COM AS OPÇÕES POSSÍVEIS;
    
    match (opcoes_1):

        #NESTE PRIMEIRO CASE O USUÁRIO DEVE CADASTRAS UM HÓSPEDE DE CADA VEZ;
        #DESTA FORMA AO REALIZAR O CHECK-OUT DE ALGUM DOS HÓSPEDES O QUARTO QUE ESTIVER LIVRE SERÁ O QUE APARECERÁ PARA CADASTRO;
        #CASO NÃO HAJA NENHUM QUARTO DISPONÍVEL APARECERÁ UMA INFORMAÇÃO DIZENDO QUE NÃO HÁ QUARTOS DISPONÍVEIS;

        case 1:
            cont_1 = 0
            while cont_1 == 0:
                if quarto_1 == 0:
                    print("-- CADASTRO DE HÓSPEDES --")
                    hospede_1 = input("ESCREVA O NOME DO HÓSPEDE: ")
                    print("VOCÊ ESTÁ NO QUARTO 01")
                    entrada_1 = (input("DATA DE ENTRADA: "))
                    saida_1 = (input("DATA DE SAÍDA: "))
                    quarto_1 = 1
                    cont_1 = 1
                    break
                if quarto_2 == 0:
                    print("-- CADASTRO DE HÓSPEDES --")
                    hospede_2 = input("ESCREVA O NOME DO HÓSPEDE: ")
                    print("VOCÊ ESTÁ NO QUARTO 02")
                    entrada_2 = (input("DATA DE ENTRADA: "))
                    saida_2 = (input("DATA DE SAÍDA: "))
                    quarto_2 = 1
                    cont_1 = 1
                    break
                if quarto_3 == 0:
                    print("-- CADASTRO DE HÓSPEDES --")
                    hospede_3 = input("ESCREVA O NOME DO HÓSPEDE: ")
                    print("VOCÊ ESTÁ NO QUARTO 03")
                    entrada_3 = (input("DATA DE ENTRADA: "))
                    saida_3 = (input("DATA DE SAÍDA: "))
                    quarto_3 = 1
                    cont_1 = 1
                    break
                if quarto_4 == 0:
                    print("-- CADASTRO DE HÓSPEDES --")
                    hospede_4 = input("ESCREVA O NOME DO HÓSPEDE: ")
                    print("VOCÊ ESTÁ NO QUARTO 04")
                    entrada_4 = (input("DATA DE ENTRADA: "))
                    saida_4 = (input("DATA DE SAÍDA: "))
                    quarto_4 = 1
                    cont_1 = 1
                    break
                if quarto_5 == 0:
                    print("-- CADASTRO DE HÓSPEDES --")
                    hospede_5 = input("ESCREVA O NOME DO HÓSPEDE: ")
                    print("VOCÊ ESTÁ NO QUARTO 05")
                    entrada_5 = (input("DATA DE ENTRADA: "))
                    saida_5 = (input("DATA DE SAÍDA: "))
                    quarto_5 = 1
                    cont_1 = 1
                    break
                if quarto_1 != 0 and quarto_2 != 0 and quarto_3 != 0 and quarto_4 != 0 and quarto_5 != 0:
                    print("NÃO HÁ QUARTOS DISPONÍVEIS NO MOMENTO!")
                    break
        
        #NO SEGUNDO CASE O USUÁRIO TERÁ NO DISPLAY APENAS OS QUARTOS QUE ESTÃO DISPONÍVEIS PARA CHACK-IN;
        #AS VARIÁVEIS DEFINIDAS COM VALOR ZERO ANTES DO INICIO DO CÓDIGO SERVEM PARA DEFINIR QUE TODOS OS QUARTOS ESTÃO DISPONÍVEIS ATÉ QUE ESSA VARIÁVEL RECEBA OUTRO VALOR E SE TORNE INDISPONÍVEL APÓS O CHECK-IN; 

        case 2:
            print("-- QUARTOS DISPONÍVEIS --")
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

        #NO TERCEIRO CASE O USUÁRIO TERÁ NO DISPLAY UM MOSTRANDO O REGISTRO DE ENTRADA E PREVISÃO DE SAÍDA DE CADA QUARTO
        #UM NOVO MENU APARECERÁ PARA QUE ELE ESCOLHA ENTRE ATUALIZAR A PREVISÃO DE SAÍDA OU REALIZAR O CHECK-OUT DO HÓSPEDE;
        #CASO O USUÁRIO ESCOLHA ALGUMA OPÇÃO QUE NÃO ESTEJA DISPONÍVEL ELE RECEBERÁ UMA MENSAGEM DE AVISO E O MENU TORNARÁ A APARECER COM AS OPÇÕES POSSÍVEIS;

        case 3:
            print("-- REGISTRO ENTRADA E SAÍDA --")
            if quarto_1 != 0:
                print(f"QUARTO 01 - ENTRADA:{entrada_1} / PREVISÃO DE SAÍDA:{saida_1}")
            if quarto_2 != 0:
                print(f"QUARTO 02 - ENTRADA:{entrada_2} / PREVISÃO DE SAÍDA:{saida_2}")
            if quarto_3 != 0:
                print(f"QUARTO 03 - ENTRADA:{entrada_3} / PREVISÃO DE SAÍDA:{saida_3}")
            if quarto_4 != 0:
                print(f"QUARTO 04 - ENTRADA:{entrada_4} / PREVISÃO DE SAÍDA:{saida_4}")
            if quarto_5 != 0:
                print(f"QUARTO 05 - ENTRADA:{entrada_5} / PREVISÃO DE SAÍDA:{saida_5}")
    
            #FOI DEFINIDO OUTRO LOOP PARA APARECER O MENU DE OPÇÕES ATÉ QUE O USUÁRIO ESCOLHA FINALIZAR AS OPERAÇÕES E VOLTAR PARA O PRIMEIRO MENU;

            cont_1 = 1
            while cont_1 > 0:
                print("-- MENU --\n1 - ATUALIZAR PREVISÃO DE SAÍDA\n2 - CHECK-OUT\n0 - SAIR")
                opcoes_2 = int(input("QUAL OPÇÃO VOCÊ DESEJA ACESSAR: "))
                
                #USAREI A ESTRUTURA MATCH CASE PARA QUE O USUÁRIO ESCOLHA ENTRE AS OPÇÕES DISPONIVEIS OU PARA QUE O SISTEMA SE ENCERRE;
                #CASO O USUÁRIO ESCOLHA ALGUMA OPÇÃO QUE NÃO ESTEJA DISPONÍVEL ELE RECEBERÁ UMA MENSAGEM DE AVISO E O MENU TORNARÁ A APARECER COM AS OPÇÕES POSSÍVEIS;

                match (opcoes_2):
                    
                    #NESTE PRIMEIRO CASE O USUÁRIO ESCOLHEU ATUALIZAR A PREVISÃO DE SAÍDA DO HÓSPEDE;
                    #O USUÁRIO PODERÁ ESCOLHER QUAL DOS QUARTOS ELE DESEJA FAZER ESSA ATUALIZAÇÃO DE ACORDO COM OS QUARTOS QUE ESTÃO OCUPADOS;
                    #CASO O USUÁRIO ESCOLHA ALGUMA OPÇÃO QUE NÃO ESTEJA DISPONÍVEL ELE RECEBERÁ UMA MENSAGEM DE AVISO E O MENU TORNARÁ A APARECER COM AS OPÇÕES POSSÍVEIS;
                    #FOI COLOCADO UM LEITOR DE CARACTERES NO INÍCIO DO CASE PARA QUE ELE RODE APENAS SE A VARIÁVEL NÃO ESTIVER VAZIA;
                    #DESTA FORMA CASO O USUÁRIO ESCOLHA A OPÇÃO 3 ANTES DE FAZER O CADASTRO DE ALGUM HÓSPEDE ELE RECEBERÁ A MENSAGEM DE QUE NÃO HÁ HÓSPEDES CADASTRADOS;

                    case 1:
                        print("-- ATUALIZAR DATA DE SAÍDA --")
                        if len(hospede_1) > 0 or len(hospede_2)  > 0 or len(hospede_3) > 0 or len(hospede_4) > 0 or len(hospede_5) > 0:
                            opcoes_3 = int(input("QUAL QUARTO VOCÊ DESEJA ATUALIZA: "))
                            
                            #USAREI A ESTRUTURA MATCH CASE PARA QUE O USUÁRIO ESCOLHA ENTRE AS OPÇÕES DISPONIVEIS PARA ATUALIZAÇÃO DA PREVISÃO DE SAÍDA;
                            #AO ESCOLHER UM DOS QUARTOS PARA REALIZAR A AUTALIZAÇÃO DE SAÍDA A VARIÁVEL QUE GUARDA A INFORMAÇÃO DE SAÍDA ANTIGA AGORA GUARDARÁ A NOVA DATA INFORMADA;

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
                    
                    #NESTE SEGUNDO CASE O USUÁRIO ESCOLHEU REALIZAR O CHECK-OUT DO HÓSPEDE;
                    #O USUÁRIO PODERÁ ESCOLHER QUAL DOS QUARTOS ELE DESEJA FAZER O CHECK-OUT DE ACORDO COM OS QUARTOS QUE ESTÃO OCUPADOS;
                    #CASO O USUÁRIO ESCOLHA ALGUMA OPÇÃO QUE NÃO ESTEJA DISPONÍVEL ELE RECEBERÁ UMA MENSAGEM DE AVISO E O MENU TORNARÁ A APARECER COM AS OPÇÕES POSSÍVEIS;
                    #FOI COLOCADO UM LEITOR DE CARACTERES NO INÍCIO DO CASE PARA QUE ELE RODE APENAS SE A VARIÁVEL NÃO ESTIVER VAZIA;
                    #DESTA FORMA CASO O USUÁRIO ESCOLHA A OPÇÃO 3 ANTES DE FAZER O CADASTRO DE ALGUM HÓSPEDE ELE RECEBERÁ A MENSAGEM DE QUE NÃO HÁ HÓSPEDES CADASTRADOS;

                    case 2:
                        print("-- CHECK-OUT --")
                        if len(hospede_1) > 0 or len(hospede_2)  > 0 or len(hospede_3) > 0 or len(hospede_4) > 0 or len(hospede_5) > 0:
                            opcoes_3 = int(input("QUAL QUARTO VOCÊ DESEJA REALIZAR CHECH-OUT: "))
                            
                            #USAREI A ESTRUTURA MATCH CASE PARA QUE O USUÁRIO ESCOLHA ENTRE AS OPÇÕES DISPONIVEIS PARA CHECK-OUT;
                            #AO ESCOLHER UM DOS QUARTOS PARA REALIZAR O CHECK-OUT A VARIÁVEL DE STATUS DEIXA DE VALER 1 E RECEBE O VALOR DE 0;
                            #AS VARIÁVEIS COM VALOR 1 SERVEM PARA DEFINIR QUE O QUARTO ESTÁ INDISPONÍVEL ATÉ QUE ESSA VARIÁVEL RECEBA O VALOR 0 E SE TORNE DISPONÍVEL APÓS O CHECK-OUT; 

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
                                
                                 #NO CASE INDEFINIDO O USUÁRIO RECEBERÁ UMA MENSAGEM DE AVISO PARA QUE ELE SAIBA QUE ESCOLHEU UMA OPÇÃO INVÁLIDA E O MENU TORNARÁ A APARECER COM AS OPÇÕES POSSÍVEISTERÁ NO DISPLAY;

                                case _:
                                    print("OPÇÃO INVÁLIDA!")
                        else:
                            print("NENHUM HÓSPEDE CADASTRADO!")
                    
                    #NO CASE 0 O USUÁRIO OPTOU PELA SAÍDA TOTAL DO SISTEMA;

                    case 0:
                        cont_1 = 0
                    
                    #NO CASE INDEFINIDO O USUÁRIO RECEBERÁ UMA MENSAGEM DE AVISO PARA QUE ELE SAIBA QUE ESCOLHEU UMA OPÇÃO INVÁLIDA E O MENU TORNARÁ A APARECER COM AS OPÇÕES POSSÍVEISTERÁ NO DISPLAY;

                    case _:
                        print("OPÇÃO INVÁLIDA!")
        
        #NO QUARTO CASE O USUÁRIO TERÁ NO DISPLAY TODOS OS QUARTOS CADASTRADOS COM OS DADOS DO NOME DO HÓSPEDE, DATA DE ENTRADA E PREVISÃO DE SAÍDA;
        #AS VARIÁVEIS DEFINIDAS COM VALOR ZERO ANTES DO INICIO DO CÓDIGO SERVEM PARA DEFINIR QUE TODOS OS QUARTOS ESTÃO DISPONÍVEIS ATÉ QUE ESSA VARIÁVEL RECEBA OUTRO VALOR E SE TORNE INDISPONÍVEL APÓS O CHECK-IN; 
        #FOI COLOCADO UM LEITOR DE CARACTERES NO INÍCIO DO CASE PARA QUE ELE RODE APENAS SE A VARIÁVEL NÃO ESTIVER VAZIA;
        #DESTA FORMA CASO O USUÁRIO ESCOLHA A OPÇÃO 4 ANTES DE FAZER O CADASTRO DE ALGUM HÓSPEDE ELE RECEBERÁ A MENSAGEM DE QUE NÃO HÁ HÓSPEDES CADASTRADOS;

        case 4:
            if len(hospede_1) > 0 or len(hospede_2)  > 0 or len(hospede_3) > 0 or len(hospede_4) > 0 or len(hospede_5) > 0:
                if quarto_1 == 1:
                    print(f"-- QUARTO 01 --\nNOME: {hospede_1} - ENTRADA: {entrada_1} - PREVISÃO DE SAÍDA: {saida_1}")
                if quarto_2 == 1:
                    print(f"-- QUARTO 02 --\nNOME: {hospede_2} - ENTRADA: {entrada_2} - PREVISÃO DE SAÍDA: {saida_2}")
                if quarto_3 == 1:
                    print(f"-- QUARTO 03 --\nNOME: {hospede_3} - ENTRADA: {entrada_3} - PREVISÃO DE SAÍDA: {saida_3}")
                if quarto_4 == 1:
                    print(f"-- QUARTO 04 --\nNOME: {hospede_4} - ENTRADA: {entrada_4} - PREVISÃO DE SAÍDA: {saida_4}")
                if quarto_5 == 1:
                    print(f"-- QUARTO 05 --\nNOME: {hospede_5} - ENTRADA: {entrada_5} - PREVISÃO DE SAÍDA: {saida_5}")
            else:
                print("NENHUM HÓSPEDE CADASTRADO!")
        
        #NO CASE 0 O USUÁRIO OPTOU PELA SAÍDA TOTAL DO SISTEMA;

        case 0:
            cont = 0
        
        #NO CASE INDEFINIDO O USUÁRIO RECEBERÁ UMA MENSAGEM DE AVISO PARA QUE ELE SAIBA QUE ESCOLHEU UMA OPÇÃO INVÁLIDA E O MENU TORNARÁ A APARECER COM AS OPÇÕES POSSÍVEISTERÁ NO DISPLAY;

        case _:
                print("OPÇÃO INVÁLIDA!")