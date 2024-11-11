#DEFININDO VARIÁVEIS VAZIAS PARA GANHAR VALORES NO DECORRER DO CÓDIGO;
#ESSAS VARIÁVEIS SERÃO ESSENCIAIS PARA MOSTRAR A SITUAÇÃO DE EMPRESTIMO DOS LIVROS E TAMBÉM PARA AVISAR AO USUÁRIO CASO ELE ACESSE QUALQUER UMA DAS OPÇÕES DE PESQUISA ANTES DE FAZER O CADASTRO DOS LIVROS;

livro_1 = ""
emprestimo_1, emprestimo_2, emprestimo_3, emprestimo_4, emprestimo_5 = 0, 0, 0, 0, 0
emp_1, emp_2, emp_3, emp_4, emp_5 = "", "", "", "", ""

#INICIO O CÓDIGO COM UM LOOP PARA APARECER O MENU DE OPÇÕES ATÉ QUE O USUÁRIO ESCOLHA FINALIZAR AS OPERAÇÕES;

cont = 1
while cont > 0: 

    #MENU COM AS OPÇÕES DISPONÍVEIS PARA O USUÁRIO;

    print("SEJA BEM-VINDO(A) A BIBLIOTECA")
    print("-- MENU --\n1 - CADASTRO\n2 - CONSULTA DE LIVROS DISPONÍVEIS\n3 - EMPRESTIMOS E DEVOLUÇÕES\n4 - LIVROS CADASTRADOS\n0 - SAIR")
    opcoes_1 = int(input("QUAL OPÇÃO VOCÊ DESEJA ACESSAR: "))

    #USAREI A ESTRUTURA MATCH CASE PARA QUE O USUÁRIO ESCOLHA ENTRE AS OPÇÕES DISPONIVEIS OU PARA QUE O SISTEMA SE ENCERRE;
    #CASO O USUÁRIO ESCOLHA ALGUMA OPÇÃO QUE NÃO ESTEJA DISPONÍVEL ELE RECEBERÁ UMA MENSAGEM DE AVISO E O MENU TORNARÁ A APARECER COM AS OPÇÕES POSSÍVEIS;

    match (opcoes_1):

        #NESTE PRIMEIRO CASE O USUÁRIO DEVE CADASTRAS OS 5 LIVROS QUE FICARÃO DISPONÍVEIS NA BILIOTECA;
        #O USUÁRIO ESTÁ RESTRITO A CADASTRAR TODOS OS LIVROS DE UMA VEZ E CASO QUEIRA ATUALIZAR A LISTA DE LIVROS, ELE PRECISARÁ RECADASTRAR TODOS OS LIVROS NOVAMENTE;

        case 1:
            print("-- CADASTRO DE LIVROS --")
            livro_1 = input("ESCREVA O NOME DO 1º LIVRO: ")
            autor_1 = input("ESCREVA O AUTOR DO 1º LIVRO: ")
            ano_1 = int(input("ESCREVA O ANO DE PUBLICAÇÃO DO 1º LIVRO: "))
            livro_2 = input("ESCREVA O NOME DO 2º LIVRO: ")
            autor_2 = input("ESCREVA O AUTOR DO 2º LIVRO: ")
            ano_2 = int(input("ESCREVA O ANO DE PUBLICAÇÃO DO 2º LIVRO: "))
            livro_3 = input("ESCREVA O NOME DO 3º LIVRO: ")
            autor_3 = input("ESCREVA O AUTOR DO 3º LIVRO: ")
            ano_3 = int(input("ESCREVA O ANO DE PUBLICAÇÃO DO 3º LIVRO: "))
            livro_4 = input("ESCREVA O NOME DO 4º LIVRO: ")
            autor_4 = input("ESCREVA O AUTOR DO 4º LIVRO: ")
            ano_4 = int(input("ESCREVA O ANO DE PUBLICAÇÃO DO 4º LIVRO: "))
            livro_5 = input("ESCREVA O NOME DO 5º LIVRO: ")
            autor_5 = input("ESCREVA O AUTOR DO 5º LIVRO: ")
            ano_5 = int(input("ESCREVA O ANO DE PUBLICAÇÃO DO 5º LIVRO: "))

        #NO SEGUNDO CASE O USUÁRIO TERÁ NO DISPLAY APENAS OS LIVROS QUE ESTÃO DISPONÍVEIS PARA EMPRESTIMO;
        #AS VARIÁVEIS DEFINIDAS COM VALOR ZERO ANTES DO INICIO DO CÓDIGO SERVEM PARA DEFINIR QUE TODOS OS LIVROS ESTÃO DISPONÍVEIS ATÉ QUE ESSA VARIÁVEL RECEBA OUTRO VALOR E SE TORNE INDISPONÍVEL APÓS O EMPRESTIMO; 
        #FOI COLOCADO UM LEITOR DE CARACTERES NO INÍCIO DO CASE PARA QUE ELE RODE APENAS SE A VARIÁVEL NÃO ESTIVER VAZIA;
        #DESTA FORMA CASO O USUÁRIO ESCOLHA A OPÇÃO 2 ANTES DE FAZER O CADASTRO DOS LIVROS ELE RECEBERÁ A MENSAGEM DE QUE NÃO HÁ NENHUM LIVRO CADASTRADO;
        #O LEITOR DE CARACTERES ESTÁ ATRELADO APENAS AO LIVRO 01 UMA VEZ QUE TENDO O PRIMEIRO LIVRO CADASTRADO O USUÁRIO SERÁ OBRIGADO A CADASTRAS TODOS OS OUTROS LIVROS SUBSQUENTEMENTE;
        #SENDO DESNECESSÁRIO A CONFERENCIA DE CARACTERES DE TODAS AS VARIÁVEIS DE CADA LIVRO;
        
        case 2:
            print("-- LIVROS DISPONÍVEIS --")
            if len(livro_1) > 0:
                if emprestimo_1 == 0:
                    print(f"{livro_1}, {autor_1}, ANO {ano_1}")
                if emprestimo_2 == 0:
                    print(f"{livro_2}, {autor_2}, ANO {ano_2}")
                if emprestimo_3 == 0:
                    print(f"{livro_3}, {autor_3}, ANO {ano_3}")
                if emprestimo_4 == 0:
                    print(f"{livro_4}, {autor_4}, ANO {ano_4}")
                if emprestimo_5 == 0:
                    print(f"{livro_5}, {autor_5}, ANO {ano_5}")
                if emprestimo_1 == 1 and emprestimo_2 == 1 and emprestimo_3 == 1 and emprestimo_4 == 1 and emprestimo_5 == 1:
                    print("NENHUM LIVRO DISPONÍVEL NO MOMENTO!")
            else:
                print("NENHUM LIVRO CADASTRADO!")

        #NO TERCEIRO CASE O USUÁRIO TERÁ NO DISPLAY UM NOVO MENU PARA QUE ELE ESCOLHA ENTRE EMPRESTIMO OU DEVOLUÇÃO DE ALGUM LIVRO;
        #CASO O USUÁRIO ESCOLHA ALGUMA OPÇÃO QUE NÃO ESTEJA DISPONÍVEL ELE RECEBERÁ UMA MENSAGEM DE AVISO E O MENU TORNARÁ A APARECER COM AS OPÇÕES POSSÍVEIS;

        case 3:
            print("-- EMPRESTIMOS E DEVOLUÇÕES LIVROS --")

            #FOI DEFINIDO OUTRO LOOP PARA APARECER O MENU DE OPÇÕES ATÉ QUE O USUÁRIO ESCOLHA FINALIZAR AS OPERAÇÕES E VOLTAR PARA O PRIMEIRO MENU;

            cont_1 = 1
            while cont_1 > 0:
                print("-- MENU --\n1 - EMPRESTIMO\n2 - DEVOLUÇÃO\n0 - SAIR")
                opcoes_2 = int(input("QUAL OPÇÃO VOCÊ DESEJA ACESSAR: "))

                #USAREI A ESTRUTURA MATCH CASE PARA QUE O USUÁRIO ESCOLHA ENTRE AS OPÇÕES DISPONIVEIS OU PARA QUE O SISTEMA SE ENCERRE;
                #CASO O USUÁRIO ESCOLHA ALGUMA OPÇÃO QUE NÃO ESTEJA DISPONÍVEL ELE RECEBERÁ UMA MENSAGEM DE AVISO E O MENU TORNARÁ A APARECER COM AS OPÇÕES POSSÍVEIS;

                match (opcoes_2):

                    #NESTE PRIMEIRO CASE O USUÁRIO ESCOLHEU FAZER UM EMPRESTIMO;
                    #APARECERÁ PARA O USUÁRIO TODOS OS LIVROS QUE ESTÃO DISPONÍVEIS PARA EMPRESTIMO;
                    #CASO O USUÁRIO ESCOLHA ALGUMA OPÇÃO QUE NÃO ESTEJA DISPONÍVEL ELE RECEBERÁ UMA MENSAGEM DE AVISO E O MENU TORNARÁ A APARECER COM AS OPÇÕES POSSÍVEIS;
                    #FOI COLOCADO UM LEITOR DE CARACTERES NO INÍCIO DO CASE PARA QUE ELE RODE APENAS SE A VARIÁVEL NÃO ESTIVER VAZIA;
                    #DESTA FORMA CASO O USUÁRIO ESCOLHA A OPÇÃO 3 ANTES DE FAZER O CADASTRO DOS LIVROS ELE RECEBERÁ A MENSAGEM DE QUE NÃO HÁ NENHUM LIVRO CADASTRADO;
                    #O LEITOR DE CARACTERES ESTÁ ATRELADO APENAS AO LIVRO 01 UMA VEZ QUE TENDO O PRIMEIRO LIVRO CADASTRADO O USUÁRIO SERÁ OBRIGADO A CADASTRAS TODOS OS OUTROS LIVROS SUBSQUENTEMENTE;
                    #SENDO DESNECESSÁRIO A CONFERENCIA DE CARACTERES DE TODAS AS VARIÁVEIS DE CADA LIVRO;

                    case 1:
                        print("-- EMPRESTIMO --")
                        if len(livro_1) > 0:
                            print("-- LISTA DE LIVROS DISPONÍVEIS--")
                            if emprestimo_1 == 0:
                                print(f"1 - {livro_1}, {autor_1}, ANO {ano_1}")
                            if emprestimo_2 == 0:
                                print(f"2 - {livro_2}, {autor_2}, ANO {ano_2}")
                            if emprestimo_3 == 0:
                                print(f"3 - {livro_3}, {autor_3}, ANO {ano_3}")
                            if emprestimo_4 == 0:
                                print(f"4 - {livro_4}, {autor_4}, ANO {ano_4}")
                            if emprestimo_5 == 0:
                                print(f"5 - {livro_5}, {autor_5}, ANO {ano_5}")
                            if emprestimo_1 == 1 and emprestimo_2 == 1 and emprestimo_3 == 1 and emprestimo_4 == 1 and emprestimo_5 == 1:
                                print("NENHUM LIVRO DISPONÍVEL NO MOMENTO!")
                            opcoes_3 = int(input("QUAL LIVRO VOCÊ DESEJA PEGAR: "))

                            #USAREI A ESTRUTURA MATCH CASE PARA QUE O USUÁRIO ESCOLHA ENTRE AS OPÇÕES DISPONIVEIS PARA EMPRESTIMO;
                            #AO ESCOLHER UM DOS LIVROS PARA PEGAR EM EMPRESTIMO A VARIÁVEL DE STATUS DEIXA DE VALER 0 E RECEBE O VALOR DE 1;
                            #AS VARIÁVEIS DEFINIDAS COM VALOR ZERO ANTES DO INICIO DO CÓDIGO SERVEM PARA DEFINIR QUE TODOS OS LIVROS ESTÃO DISPONÍVEIS ATÉ QUE ESSA VARIÁVEL RECEBA OUTRO VALOR E SE TORNE INDISPONÍVEL APÓS O EMPRESTIMO; 

                            match (opcoes_3):
                                case 1:
                                    if emprestimo_1 == 0:
                                        emprestimo_1 = 1
                                        print(f"VOCÊ ALUGOU O LIVRO {livro_1}, {autor_1}, ANO {ano_1}")
                                    else:
                                        print("LIVRO INDISPONÍVEL!")
                                case 2:
                                    if emprestimo_2 == 0:
                                        emprestimo_2 = 1
                                        print(f"VOCÊ ALUGOU O LIVRO {livro_2}, {autor_2}, ANO {ano_2}")
                                    else:
                                        print("LIVRO INDISPONÍVEL!")
                                case 3:
                                    if emprestimo_3 == 0:
                                        emprestimo_3 = 1
                                        print(f"VOCÊ ALUGOU O LIVRO {livro_3}, {autor_3}, ANO {ano_3}")
                                    else:
                                        print("LIVRO INDISPONÍVEL!")
                                case 4:
                                    if emprestimo_4 == 0:
                                        emprestimo_4 = 1
                                        print(f"VOCÊ ALUGOU O LIVRO {livro_4}, {autor_4}, ANO {ano_4}")
                                    else:
                                        print("LIVRO INDISPONÍVEL!")
                                case 5:
                                    if emprestimo_5 == 0:
                                        emprestimo_5 = 1
                                        print(f"VOCÊ ALUGOU O LIVRO {livro_5}, {autor_5}, ANO {ano_5}")
                                    else:
                                        print("LIVRO INDISPONÍVEL!")

                                #NO CASE INDEFINIDO O USUÁRIO RECEBERÁ UMA MENSAGEM DE AVISO PARA QUE ELE SAIBA QUE ESCOLHEU UMA OPÇÃO INVÁLIDA E O MENU TORNARÁ A APARECER COM AS OPÇÕES POSSÍVEISTERÁ NO DISPLAY;

                                case _:
                                    print("OPÇÃO INVÁLIDA!")
                        else:
                            print("NENHUM LIVRO CADASTRADO!")

                    #NESTE SEGUNDO CASE O USUÁRIO ESCOLHEU FAZER UMA DEVOLUÇÃO;
                    #APARECERÁ PARA O USUÁRIO TODOS OS LIVROS QUE ESTÃO DISPONÍVEIS PARA DEVOLUÇÃO;
                    #CASO O USUÁRIO ESCOLHA ALGUMA OPÇÃO QUE NÃO ESTEJA DISPONÍVEL ELE RECEBERÁ UMA MENSAGEM DE AVISO E O MENU TORNARÁ A APARECER COM AS OPÇÕES POSSÍVEIS;
                    #FOI COLOCADO UM LEITOR DE CARACTERES NO INÍCIO DO CASE PARA QUE ELE RODE APENAS SE A VARIÁVEL NÃO ESTIVER VAZIA;
                    #DESTA FORMA CASO O USUÁRIO ESCOLHA A OPÇÃO 3 ANTES DE FAZER O CADASTRO DOS LIVROS ELE RECEBERÁ A MENSAGEM DE QUE NÃO HÁ NENHUM LIVRO CADASTRADO;
                    #O LEITOR DE CARACTERES ESTÁ ATRELADO APENAS AO LIVRO 01 UMA VEZ QUE TENDO O PRIMEIRO LIVRO CADASTRADO O USUÁRIO SERÁ OBRIGADO A CADASTRAS TODOS OS OUTROS LIVROS SUBSQUENTEMENTE;
                    #SENDO DESNECESSÁRIO A CONFERENCIA DE CARACTERES DE TODAS AS VARIÁVEIS DE CADA LIVRO;

                    case 2:
                        print("-- DEVOLUÇÃO --")
                        if len(livro_1) > 0:
                            print("-- LISTA DE LIVROS DISPONÍVEIS--")
                            if emprestimo_1 == 1:
                                print(f"{livro_1}, {autor_1}, ANO {ano_1}")
                            if emprestimo_2 == 1:
                                print(f"{livro_2}, {autor_2}, ANO {ano_2}")
                            if emprestimo_3 == 1:
                                print(f"{livro_3}, {autor_3}, ANO {ano_3}")
                            if emprestimo_4 == 1:
                                print(f"{livro_4}, {autor_4}, ANO {ano_4}")
                            if emprestimo_5 == 1:
                                print(f"{livro_5}, {autor_5}, ANO {ano_5}")
                            if emprestimo_1 == 0 and emprestimo_2 == 0 and emprestimo_3 == 0 and emprestimo_4 == 0 and emprestimo_5 == 0:
                                print("NENHUM LIVRO A SER DEVOLVIDO NO MOMENTO!")
                            opcoes_3 = int(input("QUAL LIVRO VOCÊ DESEJA PEGAR: "))

                            #USAREI A ESTRUTURA MATCH CASE PARA QUE O USUÁRIO ESCOLHA ENTRE AS OPÇÕES DISPONIVEIS PARA DEVOLUÇÃO;
                            #AO ESCOLHER UM DOS LIVROS PARA FAZER A DEVOLUÇÃO A VARIÁVEL DE STATUS DEIXA DE VALER 1 E RECEBE O VALOR DE 0;
                            #AS VARIÁVEIS COM VALOR 1 SERVEM PARA DEFINIR QUE O LIVRO ESTÃO INDISPONÍVEL ATÉ QUE ESSA VARIÁVEL RECEBA O VALOR 0 E SE TORNE DISPONÍVEL APÓS O EMPRESTIMO; 

                            match (opcoes_3):
                                case 1:
                                    if emprestimo_1 == 1:
                                        emprestimo_1 = 0
                                        print(f"VOCÊ DEVOLVEU O LIVRO {livro_1}, {autor_1}, ANO {ano_1}")
                                    else:
                                        print("LIVRO NÃO ALUGADO!")
                                case 2:
                                    if emprestimo_2 == 0:
                                        emprestimo_2 = 1
                                        print(f"VOCÊ DEVOLVEU O LIVRO {livro_2}, {autor_2}, ANO {ano_2}")
                                    else:
                                        print("LIVRO NÃO ALUGADO!")
                                case 3:
                                    if emprestimo_3 == 0:
                                        emprestimo_3 = 1
                                        print(f"VOCÊ DEVOLVEU O LIVRO {livro_3}, {autor_3}, ANO {ano_3}")
                                    else:
                                        print("LIVRO NÃO ALUGADO!")
                                case 4:
                                    if emprestimo_4 == 0:
                                        emprestimo_4 = 1
                                        print(f"VOCÊ DEVOLVEU O LIVRO {livro_4}, {autor_4}, ANO {ano_4}")
                                    else:
                                        print("LIVRO NÃO ALUGADO!")
                                case 5:
                                    if emprestimo_5 == 0:
                                        emprestimo_5 = 1
                                        print(f"VOCÊ DEVOLVEU O LIVRO {livro_5}, {autor_5}, ANO {ano_5}")
                                    else:
                                        print("LIVRO NÃO ALUGADO!")

                                #NO CASE INDEFINIDO O USUÁRIO RECEBERÁ UMA MENSAGEM DE AVISO PARA QUE ELE SAIBA QUE ESCOLHEU UMA OPÇÃO INVÁLIDA E O MENU TORNARÁ A APARECER COM AS OPÇÕES POSSÍVEISTERÁ NO DISPLAY;

                                case _:
                                    print("OPÇÃO INVÁLIDA!")
                        else:
                            print("NENHUM LIVRO CADASTRADO!")

                    #NO CASE 0 O USUÁRIO OPTOU PELA SAÍDA TOTAL DO SISTEMA;

                    case 0:
                        cont_1 = 0

                    #NO CASE INDEFINIDO O USUÁRIO RECEBERÁ UMA MENSAGEM DE AVISO PARA QUE ELE SAIBA QUE ESCOLHEU UMA OPÇÃO INVÁLIDA E O MENU TORNARÁ A APARECER COM AS OPÇÕES POSSÍVEISTERÁ NO DISPLAY;

                    case _:
                        print("OPÇÃO INVÁLIDA!")

        #NO QUARTO CASE O USUÁRIO TERÁ NO DISPLAY TODOS OS LIVROS CADASTRADOS COM O STATUS DE DISPONÍVEIS E INDISPONÍVEIS PARA EMPRESTIMO;
        #AS VARIÁVEIS DEFINIDAS COM VALOR ZERO ANTES DO INICIO DO CÓDIGO SERVEM PARA DEFINIR QUE TODOS OS LIVROS ESTÃO DISPONÍVEIS ATÉ QUE ESSA VARIÁVEL RECEBA OUTRO VALOR E SE TORNE INDISPONÍVEL APÓS O EMPRESTIMO; 
        #FOI COLOCADO UM LEITOR DE CARACTERES NO INÍCIO DO CASE PARA QUE ELE RODE APENAS SE A VARIÁVEL NÃO ESTIVER VAZIA;
        #DESTA FORMA CASO O USUÁRIO ESCOLHA A OPÇÃO 4 ANTES DE FAZER O CADASTRO DOS LIVROS ELE RECEBERÁ A MENSAGEM DE QUE NÃO HÁ NENHUM LIVRO CADASTRADO;
        #O LEITOR DE CARACTERES ESTÁ ATRELADO APENAS AO LIVRO 01 UMA VEZ QUE TENDO O PRIMEIRO LIVRO CADASTRADO O USUÁRIO SERÁ OBRIGADO A CADASTRAS TODOS OS OUTROS LIVROS SUBSQUENTEMENTE;
        #SENDO DESNECESSÁRIO A CONFERENCIA DE CARACTERES DE TODAS AS VARIÁVEIS DE CADA LIVRO;

        case 4:
            print("-- LIVROS CADASTRADOS --")
            if len(livro_1) > 0:
                if emprestimo_1 == 0:
                    emp_1 = "DISPONÍVEL"
                if emprestimo_2 == 0:
                    emp_2 = "DISPONÍVEL"
                if emprestimo_3 == 0:
                    emp_3 = "DISPONÍVEL"
                if emprestimo_4 == 0:
                    emp_4 = "DISPONÍVEL"
                if emprestimo_5 == 0:
                    emp_5 = "DISPONÍVEL"
                if emprestimo_1 == 1:
                    emp_1 = "INDISPONÍVEL"
                if emprestimo_2 == 1:
                    emp_2 = "INDISPONÍVEL"
                if emprestimo_3 == 1:
                    emp_3 = "INDISPONÍVEL"
                if emprestimo_4 == 1:
                    emp_4 = "INDISPONÍVEL"
                if emprestimo_5 == 1:
                    emp_5 = "INDISPONÍVEL"
                
                print(f"1 - {livro_1}, {autor_1}, ANO {ano_1} - SITUAÇÃO {emp_1}\n2 - {livro_2}, {autor_2}, ANO {ano_2} - SITUAÇÃO {emp_2}\n3 - {livro_3}, {autor_3}, ANO {ano_3} - SITUAÇÃO {emp_3}\n4 - {livro_4}, {autor_4}, ANO {ano_4} - SITUAÇÃO {emp_4}\n5 - {livro_5}, {autor_5}, ANO {ano_5} - SITUAÇÃO {emp_5}")
            
            else:
                print("NENHUM LIVRO CADASTRADO!")
        
        #NO CASE 0 O USUÁRIO OPTOU PELA SAÍDA TOTAL DO SISTEMA;

        case 0:
            cont = 0

        #NO CASE INDEFINIDO O USUÁRIO RECEBERÁ UMA MENSAGEM DE AVISO PARA QUE ELE SAIBA QUE ESCOLHEU UMA OPÇÃO INVÁLIDA E O MENU TORNARÁ A APARECER COM AS OPÇÕES POSSÍVEISTERÁ NO DISPLAY;

        case _:
            print("OPÇÃO INVÁLIDA!")