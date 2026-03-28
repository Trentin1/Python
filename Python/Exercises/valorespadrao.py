def greet(name, greeting="Hello"):
    print(name, greeting)


greet("John")
# Output: John Hello

greet("John", "welcome")
# Output: John welcome

# You can have multiples standar arguments


def describe_person(name, age=25, city="Unknown"):
    print(f"{name} is {age} years old and lives in {city}")


describe_person("Alice")
# Uses both defautls
describe_person("Bob", 30)
# Uses defaults city
describe_person("Charlie", 35, "New York")
# Uses no defaults
