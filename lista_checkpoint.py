## Dados para teste
## email - alberico@fiap.com.br
## CNPJ - 25.540.199/0001-71
## CPF - 426.908.840-03
## Placa - lvs-6618

## Aluno - Bruno dos Santos Reis Curti - RM 84243 - 1TDCF
### Professor, sei que global nao deve ser utilizado mas nao estava conseguindo fazer o loop funcionar de maneira alguma, e com ele foi.


informacao = ["alberico@fiap.com.br", "email@example.com", "very.common@example.com", "email@subdomain.example.com", "firstname+lastname@example.com", "1234567890@example.com", "email@example-one.com", "email@example.name", "email@example.museum", "email@example.co.jp", "email@example.co.jp", "rafael@fiap.com.br", "paulo@fiap.com.br", "pedro@fiap.com.br", "wilson@fiap.com.br", "941.370.720-00", "455.337.980-56", "874.502.120-13", "426.908.840-03", "649.219.140-44", "043.998.800-40","571.379.990-50", "033.267.110-00", "977.799.200-97", "335.877.940-81", "302.615.360-52", "776.224.560-04", "283.635.630-80", "324.200.800-68", "532.806.150-03", "060.138.700-71", "402.237.810-70", "235.482.040-23", "720.497.750-59", "732.375.210-86", "055.966.670-56", "643.615.670-42", "719.116.860-97", "01.431.029/0001-90", "25.540.199/0001-71", "88.915.053/0001-83", "37.305.393/0001-51", "18.230.777/0001-08", "96.387.034/0001-50", "95.083.807/0001-41", "66.854.561/0001-66", "29.374.630/0001-08", "67.360.117/0001-57", "13.816.369/0001-19", "59.864.415/0001-56", "24.407.768/0001-42", "61.947.589/0001-24", "88.864.225/0001-37", "76.392.427/0001-44", "74.071.531/0001-01", "64.302.987/0001-81", "55.838.468/0001-41", "00.071.902/0001-19", "07.880.064/0001-73", "96.910.346/0001-04", "57.547.610/0001-27", "66.663.749/0001-27", "31.110.280/0001-14", "29.150.795/0001-04", "86.435.797/0001-75", "43.235.115/0001-78","muu-7943", "nab-2330", "ltu-9961", "dlb-7640", "hpw-7586", "nba-9371", "hpe-2099", "nad-5953", "hod-6823", "fyd-9710", "jhq-3624", "lvs-6618", "hqm-0574", "jym-0949", "nep-3270", "mwu-5998", "jst-6518", "muh-5632", "nae-7283", "nad-6180", "hya-4357", "hsg-7545"]
print("\33[31m______________________________________________________")
print("________\33[32mVerifique se sua informacao foi exposta\33[31m_______")
print("______________________________________________________")

tmp = 0

def inputInicial():
    global tmp
    tmp = input("\33[97mDigite seu dado: ")

inputInicial()


def checardados():
    for x in informacao:
        if x == tmp and "@" in tmp:
            
            retornodados = print("\33[34mSeu email foi exposto")
        elif x == tmp and "/" in tmp:

            retornodados = print("\33[35mSeu CNPJ foi exposto")
        elif x == tmp and "-" in tmp and len(tmp) == 14:

            retornodados = print("\33[36mSeu CPF foi exposto")
        elif x == tmp and "-" in tmp and len(tmp) == 8:

            retornodados = print("\33[92mA placa de seu carro foi exposta")
        

checardados()

i = 1 
print("\33[95mGostaria de consultar novamente?")
count = 0
while count <3:
    retentativa = input("\33[95mDigite S ou N: ").upper()
    if retentativa == "S":
        inputInicial()
        checardados()
    elif retentativa == "N":
        break
    else:
        count+=1

