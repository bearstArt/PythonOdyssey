# Գրել ծրագիր, որը կտպի 1-ից 10 թվերի քառակուսիները:
print("Task 1.")
for i in range(1, 11):
    print(i * i)

# Գրել ծրագիր, որը տրված թվերի ցուցակից կընտրի միայն դրական թվերը և կտպի դրանք:
# numbers = [-5, 3, -1, 101, -33, 44, 0, 7]
print("\nTask 2.")
numbers = [-5, 3, -1, 101, -33, 44, 0, 7]


def is_primary(number):
    if number > 0:
        print(number)


for num in numbers:
    is_primary(num)

# Գրել ծրագիր, որը կտպի 1-ից 20 միջակայքում գտնվող այն թվերը, որոնք բազմապատիկ են 3-ի:
print("\nTask 3.")
for i in range(1, 21):
    if i % 3 == 0:
        print(i)

# Գրել ծրագիր, որը կտպի տրված բառի յուրաքանչյուր տառը և իր ինդեքսը՝
# word = "Python"
print("\nTask 4.")
word = "Python"
for i in range(len(word)):
    print(f"{word[i]} : {i}")

# Պարզ հաշվիչի ստեղծում. ծրագիրը պետք է
# առաջարկի օգտատիրոջը ընտրել գործողությունը (+, -, *, /):
# ներմուծի երկու թիվ:
# կատարի ընտրված գործողությունը թվերի հետ:
# տպի արդյունքը:
print("\nTask 5.")


def calc(op, x, y):
    match op:
        case "+":
            return x + y
        case "-":
            return x - y
        case "*":
            return x * y
        case "/":
            if y == 0:
                print("Error: Cannot divide by zero!")
            else:
                return x / y
        case _:
            print("\nError! Invalid arithmetic operator.")


oper = input("Enter an arithmetic operator. (+, -, /, *):\n")
num_1 = int(input("Enter the first number:\n"))
num_2 = int(input("Enter the second number:\n"))
print(calc(oper, num_1, num_2))
