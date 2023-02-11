import random

print("[ --- Gerador de senhas --- ]\n")

caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789"

numero_caracteres = input("Quantidade de senhas a ser geradas: ")
numero_caracteres = int(numero_caracteres)

tamanho_senhas = input("Tamanho das senhas: ")
tamanho_senhas = int(tamanho_senhas)

print("\nSuas senhas estão logo abaixo: ")

continuar = True
fechar = 0

while(continuar == True):
    for pwd in range(numero_caracteres):
        senhas = ''
        for i in range(tamanho_senhas):
            senhas += random.choice(caracteres)
        print(senhas)
    fechar = input("Digite qualquer coisa para finalizar a aplicação: ")
    continuar = False

