def calcular_media(notas):
    x = sum(notas) / len(notas)
    if x >= 6:
        print("Aprovado")
    else:
        print("Reprovado")

    #snake_case é o padrão recomendado para nomes de variáveis e funções em Python
    # camelCase não é recomendado para Python e sim para java e js
    # PascalCase é recomendado para nomes de classes em Python
    # kebab-case não é recomendado para Python, é mais usado em nomes de arquivos e URLs
    # screaming_snake_case é usado para constantes em Python
    