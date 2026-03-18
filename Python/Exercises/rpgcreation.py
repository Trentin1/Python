# Criação de personagem

level = int(input("Digite o level: "))
has_training = input("Tem treinamento? (True/False): ") == "True"
level_message = "None"

if 1 <= level <= 5:
    level_message = "Basic weapons only"

elif 6 <= level <= 10 and not has_training:
    level_message = "Need weapon training first"

elif 6 <= level <= 10 and has_training:
    level_message = "Access to advanced weapons granted"

elif level >= 11:
    level_message = "Access to all weapons granted"

elif level <= 0:
    level_message = "Invalid level"

print(level_message)
