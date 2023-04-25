def decimal_to_binary(decimal):
    
    if decimal <= 0:
        return "El número decimal debe ser mayor a 0."
    else:
        binario = ""
        while decimal > 0:
            residuo = decimal % 2
            binario = str(residuo) + binario
            decimal = decimal // 2
        return binario

if __name__ == "__main__":
    input()