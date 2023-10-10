number_one = int(input("Enter first number: "))
number_two = int(input("Enter second number: "))
symbol = input("Enter symbol: ")

if symbol == "+":
    print(f"Sum: {number_one + number_two}")
elif symbol == "-":
    print(f"Difference: {number_one - number_two}")
elif symbol == "*":
    print(f"Multiplication: {number_one * number_two}")
elif symbol == "/":
    print(f"Division: {number_one / number_two}")
else:
    print("There is no such symbol in my calculator .")