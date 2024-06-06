# Ստեղծել բառարան երեք բանալի-արժեք զույգերով, որտեղ բանալիները ուսանողների անուններն են, իսկ արժեքները՝ նրանց
# գնահատականները։ Ավելացnel նոր ուսանող և նրա գնահատականը բառարանում։ Այնուհետև տպել բոլոր ուսանողների անունները և
# նրանց գնահատականները։ Փոփոխել կամայական ուսանողի գնահատականը և ջնջել մեկ այլ ուսանողի ամբթղջությամբ։
students = {"Armen": 82, "Hayk": 76, "Anna": 95}
print(students)
students["Karen"] = 67
print(students)
students["Hayk"] = 58
del students["Armen"]
print(students)


# Ստեղծեl երկու set տարբեր արժեքներով, միավորեք դրանք և տպեք վերջնական արդյունքը։
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
merged_set = set1.union(set2)
print(merged_set)


# Գրել ծրագիր, որը ցիկլերի միջոցով կտպի հետևյալ պատկերը էկրանին:
# *
# **
# ***
# ****
# *****
for i in range(1, 6):
    print("*" * i)


# Գրեք ծրագիր, որը որպես մուտքային արժեք կստանա տող և կտպի բաղաձայնների և ձայնավորների քանակը
# (կարող եք վերցնել անգլերեն այբուբենը)։
text = input("Enter a string: ")
vowels = "aeiou"
count_char = len(text)
count_vowels = 0
for char in text:
    if char.lower() in vowels:
        count_vowels += 1
print("Number of consonants:", count_char - count_vowels)
print("Number of vowels:", count_vowels)
