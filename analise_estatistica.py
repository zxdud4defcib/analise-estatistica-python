numeros = []

# Leitura dos 15 números reais
for i in range(15):
    valor = float(input(f"Digite o {i + 1}º número: "))
    numeros.append(valor)

# Cálculos principais
soma = sum(numeros)
media = soma / len(numeros)
maior = max(numeros)
menor = min(numeros)

# Dobro e cubo dos números
dobros = []
cubos = []

for n in numeros:
    dobros.append(n * 2)
    cubos.append(n ** 3)

# Cálculo da porcentagem de números ímpares
impares = 0
for n in numeros:
    if n % 2 != 0:
        impares += 1

porcentagem_impares = (impares / len(numeros)) * 100

# Exibição dos resultados
print("\n📊 RESULTADOS")
print(f"Soma dos números: {soma}")
print(f"Média dos números: {media}")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
print(f"Dobro dos números: {dobros}")
print(f"Cubo dos números: {cubos}")
print(f"Porcentagem de números ímpares: {porcentagem_impares:.2f}%")