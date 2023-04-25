def binary_to_decimal(binario):

    decimal = 0
    potencia = 0
    while binario != 0:
        digito = binario % 10
        decimal += digito * (2 ** potencia)
        binario = binario // 10
        potencia += 1
    return decimal

if __name__ == '__main__':
    input()