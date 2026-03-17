# CoddyTechExercise

print("Bill Split Calculator")

bill_amount = float(input("Digite o valor da conta: "))
tip_percentage = float(input("Digite a porcetagem da gorjeta: "))
people = int(input("Digite o número de pessoas: "))

tip_amount = (tip_percentage / 100) * bill_amount
total_amount = bill_amount + tip_amount
amount_per_people = (total_amount / people)
print(f"Total (including tip): ${total_amount}")
print(f"Each person pays: ${amount_per_people}")
