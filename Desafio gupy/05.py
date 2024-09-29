def inverter_string(s):

    """
    Inverte os caracteres de uma string.
    """

    string_invertida = "" 

    for i in range(len(s) - 1, -1, -1):  
        string_invertida += s[i]  

    return string_invertida

entrada = input("Informe uma string para ser invertida: ")

resultado = inverter_string(entrada)

print(f"String invertida: {resultado}")
