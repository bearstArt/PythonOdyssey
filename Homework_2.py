print("\nEnter parameters for conversion!!")
choice = int(input("1. Convert kg to pounds\n"
                   "2. Convert pounds to kg"
                   "\n\n\tchoice: "))


def convert_kg_to_pounds(kg):
    return kg * 2.20462


def convert_pounds_to_kg(pounds):
    return pounds * 0.453592


weight = int(input("Please enter the weight: "))

if choice == 1:
    print(f'{convert_kg_to_pounds(weight)} kg')
elif choice == 2:
    print(f'{convert_pounds_to_kg(weight)} pounds')
else:
    print("Error! Wrong input!")
