from random import randint
from datetime import date

#Caso o Número de Hóspedes for 0 ele vai pedir senha para encerrar o programa
encerrar = ''

# LISTA DE HÓSPEDES
ListaNome = []
ListaIdade = []
ListaCpf = []
ListaEndereco = []
ListaCertidao = []

# LISTA DE QUARTOS
ListaTipoComum = []
ListaTipoSuite = []
ListaTipoLuxo = []

# LISTA DE LOGIN
ListaLogin = []
ListaSenha = []

# Função para Calcular Idade recebendo Dia, mês e Ano de nascimento.
def calculoIdade():
    diaNascimento = int(input("Informe o dia de Nascimento: "))
    mesNasimento = int(input("Informe o mês de Nascimento: "))
    anoNascimento = int(input("Informe o ano de Nascimento: "))
    dataNascimento = date(anoNascimento, mesNasimento, diaNascimento)
    diferenca = date.today() - dataNascimento
    idade = (diferenca.days / 365.25)
    return idade

while encerrar != 'receptsmart':
    print('PROGRAMA DE CHECK IN/OUT CHMABRES')
    pergunta1 = str(input("Você possui um número de Reserva? (S/N): ")).upper()

    if pergunta1 == 'S':
        nReserva = int(input("Insira o seu número de Reserva da Booking: "))
        #Coleta as informações do Booking como Tipo de Quarto, Quantidade de Hóspedes e preenche com as informações recebidas.
        #Após isso, o programa pede para validar as informações preenchidas automaticamente e completar as informações restantes.
        #Segue a mesma lógica abaixo:
        
    elif pergunta1 == 'N':
        nHospedes = int(input("Vamos fazer o Check-In Agora! Informe a Quantidade de Hóspedes: "))
        if nHospedes == 0:
            encerrar = input("Se você realmente deseja encerrar, digite a senha: ")
            if encerrar == 'receptsmart':
                print("Programa Finalizado.")
                break
        tipo = int(input("Informe o tipo de quarto que irá reservar (1-Comum, 2-Suíte, 3-Luxo): "))
        
        # Reservando o Quarto e Verificando se está vago.
        if tipo == 1:
            if len(ListaTipoComum) < 5:
                quarto = randint(101,105)
                if quarto in ListaTipoComum:
                    while quarto in ListaTipoComum:
                        quarto = randint(101,105)
                ListaTipoComum.append(quarto)
            else:
                print("Não temos mais vagas para este tipo de quarto.")

        elif tipo == 2:
            if len(ListaTipoSuite) < 5:
                quarto = randint(201,205)
                if quarto in ListaTipoSuite:
                    while quarto in ListaTipoSuite:
                        quarto = randint(201,205)
                ListaTipoSuite.append(quarto)
            else:
                print("Não temos mais vagas para este tipo de quarto.")

        elif tipo == 3:
            if len(ListaTipoLuxo) < 5:
                quarto = randint(301,305)
                if quarto in ListaTipoLuxo:
                    while quarto in ListaTipoLuxo:
                        quarto = randint(301,305)
                ListaTipoLuxo.append(quarto)
            else:
                print("Não temos mais vagas para este tipo de quarto.")

    # Pedindo Informações dos Hóspedes
        for c in range (nHospedes):
            print(f"Hóspede {c+1}")
            idade = calculoIdade()
            ListaIdade.append(idade)
            if idade >= 18:
                nome = ListaNome.append(str(input(f'Digite o nome: ')).title())
                cpf = ListaCpf.append(int(input('Digite seu CPF: ')))
                endereco = ListaEndereco.append(str(input('Digite o Endereço: ')))
            elif idade < 18:
                nome = ListaNome.append(str(input(f'Digite o nome: ')).title())
                certidao = ListaCertidao.append(int(input("Informe o Número de Registro da Certidão de Nascimento ou RG: ")))
                #Recebe o número da certidão de Nascimento e a declaração.
    else:
        print("Dado Inválido!")

    # Listando os Hóspedes do quarto
    for c in range(nHospedes):
        print(f"Nome = {ListaNome[c]}\tIdade = {ListaIdade[c]:.0f}\tCPF = {ListaCpf[c]}\tEndereco = {ListaEndereco[c]}")

    # Definindo um Login e Verificando se há um Login igual na Lista.
    login = randint(1, 1000)
    if login in ListaLogin:
        while login in ListaLogin:
            login = randint(1,1000)
    else:
        ListaLogin.append(login)

    # Definindo uma Senha
    senha = randint(1, 1000)
    ListaSenha.append(senha)

    print(f"Seu login é: {login}\nSua senha é: {senha}")
    print(f"Você ficará no quarto {quarto}")
    print(ListaTipoComum,ListaTipoLuxo,ListaTipoSuite)

#Ao final do programa, ele coleta os dados necessários da Ficha Nacional de Registro de Hóspedes e Envia Automaticamente para o sistema
# http://www.snrhos.hospedagem.turismo.gov.br/maximo/webclient/login/login.jsp?uisessionid=1349116601551&welcome=true