i = int(input("Quantos Alunos ? "))
for i in range(0, i):

    Et1nota1 = float(input("Insira a primeira nota da Etapa 1: "))
    Et1nota2 = float(input("Insira a segunda nota da Etapa 1: "))
    Et2nota1 = float(input("Insira a primeira nota da Etapa 2: "))
    Et2nota2 = float(input("Insira a segunda nota da Etapa 2: "))
    numfaltas = int(input("Insira o número de faltas do aluno: "))
    numaulas = int(input("Insira o número de total de aulas: "))

    mediaEt1 = (Et1nota1 + Et1nota2) / 2
    mediaEt2 = (Et2nota1 + Et2nota2) / 2
    mediafinal = ((mediaEt1 * 2) + (mediaEt2 * 3)) / 5
    limite25 = (numaulas * 25) / 100

    if limite25 >= numfaltas:
        if mediafinal >= 7:
            print("Aprovado, você tirou {}".format(mediafinal))
        elif 7 > mediafinal > 3:
            print("AVALIAÇÃO FINAL, você tirou {}".format(mediafinal))
        else:
            print("Reprovado por Nota, você tirou {}".format(mediafinal))
    else:
        print("Reprovado por falta, você faltou {} vezes".format(numfaltas))
