def informacaousuario():
    while True:
        try:
            nome = input("Digite seu nome completo: ")
            data_nascimento= int(input("Digite seu ano de nascimento (entre 1922 e 2024): "))
            if 1922 <= data_nascimento <= 2021:
                break
            else:
                print("Ano de nascimento inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
    
    ano_atual = 2024 # Simulando o ano atual
    idade = ano_atual - data_nascimento
    print(f"{nome}, você completou ou completará {idade} anos em {ano_atual}.")

if __name__ == "__main__":
    informacaousuario()