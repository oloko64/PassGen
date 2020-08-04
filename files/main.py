import random
import string


def strings(checked):
    if not checked:
        a = string.ascii_letters + "0123456789"
    else:
        a = string.ascii_letters + "0123456789!@#$%&?."
    return a


def gerar(num, checked):
    text = ""
    for x in range(num):
        text += random.choice(strings(checked))
    return str(text)

# Teste das funcoes, ignore

# if __name__ == "__main__":
#     a = input("Digite o tamanho da senha desejada: ")
#     gerar(int(a))
