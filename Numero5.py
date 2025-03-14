n = list(map(int, input("Digite uma lista de números inteiros separados por espaço: ").split()))
numero_procurado = int(input("Digite o número que deseja contar: "))
print(f"O número {numero_procurado} aparece {n.count(numero_procurado)} vezes na lista.")