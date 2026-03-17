# Desafio Fácil

# Você está ajudando um app de meteorologia a determinar atividades ao ar livre adequadas
#  com base nas condições climáticas. Crie um programa que usa operações lógicas para determinar se certas atividades são possíveis.

# Inicialize as seguintes variáveis:

# is_sunny com o valor True
# temperature com o valor 25
# wind_speed com o valor 10
# water_temperature com o valor 22
# Escreva as seguintes expressões lógicas para determinar se:

# can_go_hiking: Está ensolarado AND temperatura está acima de 15°C AND velocidade do vento está abaixo de 20 km/h
# can_go_swimming: Está ensolarado AND temperatura está acima de 20°C AND temperatura da água está acima de 18°C
# cannot_go_outside: NÃO está ensolarado OR temperatura está abaixo de 10°C OR velocidade do vento está acima de 30 km/h

# Variavéis
is_sunny = True
temperature = 25
wind_speed = 10
water_temperature = 22

# Calculando as condições
can_go_hiking = is_sunny and temperature > 15 and wind_speed < 20
can_go_swimming = is_sunny and temperature > 20 and water_temperature > 18
cannot_go_outside = not is_sunny or temperature < 10 or wind_speed > 30

print("Can go hiking:", can_go_hiking)
print("Can go swimming:", can_go_swimming)
print("Cannot go outside:", cannot_go_outside)
