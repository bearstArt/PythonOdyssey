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
    print(f'{weight} kg = {convert_kg_to_pounds(weight)} pounds')
elif choice == 2:
    print(f'{weight} pounds = {convert_pounds_to_kg(weight)} kg')
else:
    print("Error! Wrong input!")
