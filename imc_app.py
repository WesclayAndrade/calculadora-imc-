print("== Vamos calcular seu imc?")
def imc(peso, altura):
    resultado = peso /(altura**2)
    return resultado
def classificacao(imc):
    if imc is None:
        raise ValueError("Ainda não existem dados para informar.")
    
    if imc < 18.5 : 
        return " **ATENÇÃO** Você está abaixo do peso ideal."
    elif imc   < 24.9:
        return "Muito bem, você está no peso adequado."
    elif imc   < 29.9:
        return "Cuidado, estamos entrando no sobrepeso.."
    elif imc   < 34.9:
        return "ATENÇÃO, atingimos a obesidade em grau I. Procure um nutricionista e um médico urgente!!"
    elif imc < 39.9:
        return "ATENÇÃO, atingimos a obesidade grau II. Procure um nutricinista e um médico urgente!!"
    else:
        return "Estamos sob risco, torna-se necessário uma intervenção urgente. Vamos cuidar de sua saúde?"
def menu(resultado_imc=None):
       
    print("Escolha uma das opções abaixo:")
    print("1. Calcular IMC.")
    print("2. Saber sua classificação de IMC.")
    print("3. Escolhar um contato profissinal.")
    print("4. Sair..")
    selecao = int(input("Qual você deseja acessar? "))
    if selecao == 1: 
        try:
            peso = float(input("Informe seu peso em KG (ex.: 80.2)? "))
            altura = float(input("Informe sua altura em metros (ex.: 1.70)?"))
            if altura <=0 or peso <=0:
                print("Peso e altura devem ser maior que zero.")
                menu(resultado_imc)
                return
            
            resultado_imc = int(imc(peso, altura))
            print(f"Seu imc atual é {resultado_imc: .2f} ")
            menu(resultado_imc)
            return
        except ValueError:
            print("Entrada inválida! Digite apenas números válidos!")

    elif selecao == 2:
        try: 
            classificar_imc = classificacao(resultado_imc)
            print(f"Seu IMC é {resultado_imc: .2f} e a sua classificação é: {classificacao}")
        except ValueError as erro:
            print(f"Atenção: {erro}")
            print("Escolha a opção 1 primeiro para regisdtrar seu peso e altura.")
            menu(resultado_imc)
    elif selecao == 3:
            print("1. Nutricionista")
            print("2. Personal")
            print("3. Médico")
            profissional = int(input("Qual você deseja o contato:"))
            if profissional == 1:
                print("Segue o Telefone do nutricionista 999999999")
                menu(resultado_imc)
                return
            elif profissional == 2:
                print("Segue o telefone do personal 9999999999")
                menu(resultado_imc)
                return
            elif profissional == 3:
                print("Segue o telefone do médico ")
                menu(resultado_imc)
                return
    elif selecao == 4:
        print("Saindo...")
        return

  
if __name__ == "__main__":
    selecao = menu()