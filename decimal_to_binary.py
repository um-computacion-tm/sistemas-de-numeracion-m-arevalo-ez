def decimal_to_binary(decimal):
    b = 0
    while decimal >= 2:
        x = decimal // 2
        if x == 1:
            b += x
        elif x == 0:
            b += x
 
    y = decimal % 2
    z = 0
    z += y
    while decimal >= 2:
        i = str(decimal // 2)
        z += i
    
    z = z[::-1]
    b += z
    return b

if __name__ == "__main__":
    input()