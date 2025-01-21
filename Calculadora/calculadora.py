def calculadora():
    while True:
        print("\nEscolha uma operação:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        opcao = input("Digite o número para a operação correspondente: ")

        if opcao == '0':
            print("Saindo...")
            break
        elif opcao in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Digite o primeiro valor: "))
                num2 = float(input("Digite o segundo valor: "))
            except ValueError:
                print("Valores inválidos. Tente novamente.")
                continue

            if opcao == '1':
                resultado = num1 + num2
                print(f"Resultado da soma: {resultado}")
            elif opcao == '2':
                resultado = num1 - num2
                print(f"Resultado da subtração: {resultado}")
            elif opcao == '3':
                resultado = num1 * num2
                print(f"Resultado da multiplicação: {resultado}")
            elif opcao == '4':
                if num2 != 0:
                    resultado = num1 / num2
                    print(f"Resultado da divisão: {resultado}")
                else:
                    print("Erro: Divisão por zero não é permitida.")
        else:
            print("Essa opção não existe. Tente novamente.")

if __name__ == "__main__":
    calculadora()