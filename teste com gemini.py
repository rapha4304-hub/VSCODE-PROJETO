# Passo 1: Receber e converter a entrada
numero = int(input("Digite um número para saber se é par ou ímpar: "))

# Passo 2: Fazer a Decisão com if/else

if numero % 2 == 0:
    # Se a condição for VERDADEIRA (resto é 0, ou seja, é PAR)
    print("O número", numero, "é PAR.")
else:
    # Se a condição for FALSA (resto não é 0, ou seja, é ÍMPAR)
    print("O número", numero, "é ÍMPAR.")