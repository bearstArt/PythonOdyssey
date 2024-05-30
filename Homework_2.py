weight = int(input("Please enter the weight: "))
print("Enter the various for converting!")
choice = input("1. Convert kg to pounds"
               "2. Convert pounds to kg"
               "\n\t:")


def convert_kg_to_pounds(kg):
    return kg * 2.20462

def convert_pounds_to_kg(pounds):
    return pounds * 0.453592

if choice == 1:
    print(convert_kg_to_pounds(weight))
elif choice == 2:
    print(convert_pounds_to_kg(weight))
else:
    print("Error! Wrong input!"

