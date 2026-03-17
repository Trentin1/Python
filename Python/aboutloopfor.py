# Estudos sobre laço for/loop for do site/app Coddy.Tech
# for i in range(start, end):

# Exemplo.:
for i in range(0, 5):
    print(i)

# Podemos simplificar o range (0, 5) para range (5).:

for i in range(5):
    print(i)

# Você também pode combinar i com outro texto usando uma f-string.
# Coloque um f antes da string e use {i} dentro dela para inserir o valor de i:

for i in range(1, 4):
    print(f"item number: {i}")

# Os laços tem muitos casos de uso. Por exmplo, vamos somar todos os números de 1 a 100:

sum_numbers = 0
for i in range(1, 101):
    sum_numbers += i
print(sum_numbers)
