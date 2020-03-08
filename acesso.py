##tipos de resposta
loginADM_M = ("Ola administrador")
loginADM_F = ("Ola administradora")

loginUSR_M = ("Ola usuario")
loginUSR_F = ("Ola usuaria")

loginGUEST = ("Ola visitante")

loginUNKW = ("Ola desconhecido")

##inputs


caixaEntradaCargo = str(input("Por favor informe o seu cargo: "))


caixaEntradaGenero = str(input("Por favor informe o seu genero: "))

if any(s.isdigit() for s in caixaEntradaCargo):
    raise ValueError("Apenas letras, por favor")

if any(s.isdigit() for s in caixaEntradaGenero):
    raise ValueError("Apenas letras, por favor")

##padronizando
caixaEntradaCargo = caixaEntradaCargo.upper()
caixaEntradaGenero = caixaEntradaGenero.upper()

##loops dos cargos
if caixaEntradaCargo == "ADM" and caixaEntradaGenero == "M":
    print (loginADM_M)
    
elif caixaEntradaCargo == "ADMINISTRADOR" and caixaEntradaGenero == "M":
    print (loginADM_M)

elif caixaEntradaCargo == "ADM" and caixaEntradaGenero == "F":
    print (loginADM_F)

elif caixaEntradaCargo == "ADMINISTRADOR" and caixaEntradaGenero == "F":
    print (loginADM_F)

if caixaEntradaCargo == "USR" and caixaEntradaGenero == "M":
    print (loginUSR_M)

elif caixaEntradaCargo == "USUARIO" and caixaEntradaGenero == "M":
    print (loginUSR_M)

elif caixaEntradaCargo == "USR" and caixaEntradaGenero == "F":
    print (loginUSR_F)

elif caixaEntradaCargo == "USUARIO" and caixaEntradaGenero == "F":
    print (loginUSR_F)

if caixaEntradaCargo == "GUEST" and caixaEntradaGenero == "M":
    print (loginGUEST)

elif caixaEntradaCargo == "GUEST" and caixaEntradaGenero == "F":
    print (loginGUEST)
    
if caixaEntradaCargo != "ADM" and caixaEntradaCargo != "ADMINISTRADOR" and caixaEntradaCargo != "USR" and caixaEntradaCargo != "USUARIO" and caixaEntradaCargo != "GUEST":
    print (loginUNKW)
