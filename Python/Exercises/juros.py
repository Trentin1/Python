# Calcule o juros de um depóisto bancário

principal = float(input("Digite o valor do depósito: R$"))
taxa = float(input("Digite a taxa de juros ao mês (%): "))
tempo = float(input("Quantos meses deseja aplicar: "))

# Converter a taxa percentual para decimal

taxa = taxa / 100

juros = principal * taxa * tempo

# Uma saída com mais clareza e organizada

print(f"\nDepósito inicial: R${principal:.2f}")
print(f"Taxa de juros: {taxa*100:.2f} ao mês")
print(f"Tempo de aplicação: {tempo: .0f} meses")
print(f"Juros acumulados: R${juros:.2f}")

# Desafio Extra!
# Adapte o programa para que ele também calcule e exiba o valor total acumulado ao final da aplicação.

valor_total = principal + juros
print(f"O valor total ao final da aplicação será de R$ {valor_total:.2f}")
