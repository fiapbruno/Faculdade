## Hospital

## Corona Virus

## Idade: 15 < or > 60; Tem risco (Prioritario)
## Caso contrario segue na fila

## variavel.title()
## variavel.upper()
## variavel.lower()
## str(variavel | int(variavel)
## input("qual a pergunta")

nomepaciente = input("Qual seu nome?")
idadepaciente = int(input("Entre sua idade:"))
riscopaciente = str(input("Voce possui diabetes, pressao alta, asma, fuma? Responda sim ou nao."))
riscopaciente = riscopaciente.upper()
riscopaciente = riscopaciente.upper()

if riscopaciente == "SIM":
        riscofinal = 1
        print("Nome adicionado a lista de risco")
elif riscopaciente == "NAO":
        riscofinal = 0
        print("Nome adicionado a lista normal")
if riscopaciente != "SIM" and riscopaciente != "NAO":  
    print ("Responda apenas sim ou nao")

while True:
    if len(riscopaciente) > 3:
        print ("Responda apenas sim ou nao")
        break
    else:
        break




faixaidadeum = 10<= idadepaciente <= 19
faixaidadedois = 20<= idadepaciente <= 29
faixaidadetres = 30<= idadepaciente <= 39
faixaidadequatro = 40<= idadepaciente <= 49
faixaidadecinco = 50<= idadepaciente <= 59
faixaidadeseis = 60<= idadepaciente <= 69
faixaidadesete = 70<= idadepaciente <= 79
faixaidadeoito = idadepaciente >= 80