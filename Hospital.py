## Hospital

## Corona Virus

## Idade: 15 < or > 60; Tem risco (Prioritario)
## Caso contrario segue na fila

## variavel.title()
## variavel.upper()
## variavel.lower()
## str(variavel | int(variavel)
## input("qual a pergunta")

nomepaciente = input("Qual seu nome? ")
idadepaciente = int(input("Entre sua idade: "))
riscopaciente = str(input("Voce possui diabetes, pressao alta, asma, fuma? Responda sim ou nao. "))
riscopaciente = riscopaciente.upper()
riscopaciente = riscopaciente.upper()
riscopositivo = 0
faixaidadezero = 0
faixaidadeum = 0
faixaidadedois = 0
faixaidadetres = 0
faixaidadequatro = 0
faixaidadecinco=  0
faixaidadeseis = 0
faixaidadesete = 0
faixaidadeoito = 0
faixaidadenove = 0

if idadepaciente <= 10:
    faixaidadezero = 1
    riscofinal = 1
elif 10<= idadepaciente <= 19:
    faixaidadeum = 1
    riscofinal = 2
elif 20<= idadepaciente <= 29:
    faixaidadedois = 1
    riscofinal = 3
elif 30<= idadepaciente <= 39:
    faixaidadetres = 1
    riscofinal = 4
elif 40<= idadepaciente <= 49:
    faixaidadequatro = 1
    riscofinal = 5
elif 50<= idadepaciente <= 59:
    faixaidadecinco =  1
    riscofinal = 6
elif 60<= idadepaciente <= 69:
    faixaidadeseis = 1
    riscofinal = 7
elif 70<= idadepaciente <= 79:
    faixaidadesete = 1
    riscofinal = 8
elif idadepaciente >= 80:
    faixaidadeoito =  1
    riscofinal = 9

if any(s.isdigit() for s in nomepaciente):
    raise ValueError("Apenas letras no campo do nome, por favor")

if any(s.isdigit() for s in riscopaciente):
    raise ValueError("Apenas sim ou nao, por favor")

if riscopaciente == "SIM" or faixaidadezero == 1 or faixaidadeseis == 1 or faixaidadesete == 1 or faixaidadeoito == 1: 
        riscopositivo = 1
        print("Paciente " + nomepaciente + " adicionado a lista de risco")
         
elif riscopaciente == "NAO" and faixaidadezero != 1 and faixaidadeseis != 1 and faixaidadesete != 1 and faixaidadeoito != 1:
        print("Paciente " + nomepaciente + " adicionado a lista normal")

if riscopaciente != "SIM" and riscopaciente != "NAO":  
    print ("Responda apenas sim ou nao")


