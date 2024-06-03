# Write a program that asks the user for weight in kilograms and converts it to pounds.
coefficient = 0.45359237
print("\nEnter parameters for conversion!!")
choice = int(input("1. Convert kg to pounds\n"
                   "2. Convert pounds to kg"
                   "\n\n\tchoice: "))


def convert_kg_to_pounds(kg):
    return kg / coefficient


def convert_pounds_to_kg(pounds):
    return pounds * coefficient


weight = int(input("Please enter the weight: "))

if choice == 1:
    print(f"{weight} kg = {convert_kg_to_pounds(weight)} pounds")
elif choice == 2:
    print(f"{weight} pounds = {convert_pounds_to_kg(weight)} kg")
else:
    print("Error! Wrong input!")


# Write a program that asks the user to enter two numbers, x, and y, and computes x − y  /  x+y.
def summ(x, y):
    return x + y


def div(x, y):
    return x / y


def sub(x, y):
    return x - y


def mat_func1(x, y):
    if summ(x, y) == 0:
        print('\"Error: Cannot divide by zero!\"')
    else:
        return div(sub(x, y), summ(x, y))


def mat_func2(x, y):
    if x == 0:
        return "Error: Cannot divide by zero!"
    else:
        return summ(sub(x, div(y, x)), y)


num1 = int(input("\nPlease enter the number 'x': "))
num2 = int(input("Please enter the number 'y': "))

print(f"\nVariant 1: (x − y) / (x + y) = {mat_func1(num1, num2)}")
print(f"Variant 2: x − (y / x) + y = {mat_func2(num1, num2)}")

