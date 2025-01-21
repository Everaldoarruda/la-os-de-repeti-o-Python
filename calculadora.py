ef calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        return num1 / num2 if num2 != 0 else 'Erro: Divisão por zero'
    else:
        return 0

# Exemplos de uso
print(calculadora(10, 5, 1))  # Soma: 15
print(calculadora(10, 5, 2))  # Subtração: 5
print(calculadora(10, 5, 3))  # Multiplicação: 50
print(calculadora(10, 5, 4))  # Divisão: 2.0
print(calculadora(10, 5, 5))  # Operação inválida: 0
