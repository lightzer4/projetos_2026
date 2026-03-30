def criar_personagem():

    print(" CRIAÇÃO DE PERSONAGEM ")
    print()


    nome  = input("NOME  : ")
    raca  = input("RAÇA  : ")
    idade = input("IDADE : ")
    level = input("LEVEL : ")

    print()


    dic = {'nome': nome, 'raca': raca, 'idade': idade, 'level': level}
    for k, v in dic.items():
        print(f"{k}: {v}")


criar_personagem()