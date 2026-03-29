print("Welcome to FizzBuzz!")


def fizzbuzz(number):
    result = ""
    if number % 3 == 0:
        result += "Fizz"
    if number % 7 == 0:
        result += "Buzz"
    if result == "":
        result = str(number)
    return result


limit = int(input())
print(fizzbuzz(limit))
