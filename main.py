import random, string


def gerar(num):
    text = ""
    a = string.ascii_letters
    for x in range(num):
        text += random.choice(a)
    return str(text)

# if __name__ == "__main__":
#     a = input("Digite o tamanho da senha desejada: ")
#     gerar(int(a))
