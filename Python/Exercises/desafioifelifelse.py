temperature = int(input("Digite a temperatura: "))
weather = "unset"

if temperature < 0:
    weather = "Freezing"

elif 0 <= temperature <= 15:
    weather = "Cold"

elif 16 <= temperature <= 25:
    weather = "Mild"

else:
    weather = "Hot"


print(f"A temperatura é {temperature}Cº e o clima está = {weather}")
