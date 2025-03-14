n = list(map(int, input("Digite uma lista de números inteiros separados por espaço: ").split()))
numeros_sem_duplicatas = list(dict.fromkeys(n))
print("Lista sem duplicatas:", numeros_sem_duplicatas)