# Laço Aninhado

for i in range(3):
    print(f"Outer loop iteration: {i}")

    for j in range(2):
        print(f" Inner loop iteration: {j}")
# Print a 2x3 rectangle of stars
for row in range(2):  # 2 rows
    line = ""
    for col in range(3):  # 3 columns
        line += "*"
    print(line)

# Output:
# ***
# ***
