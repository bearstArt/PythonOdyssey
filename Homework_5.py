print("Հայտարարել list,  որը բաղկացած է string-ներից:\n"
      "Տպել list-ում եղած ամենաերկար string-ը  և համապատասխան index-ը:\n")
ls1 = ["Hello", "Python", "Language","Programmer",  "Name", "Professor", "Super"]
print(ls1)

size_of_ls = len(ls1)
index = 0
tmp = ""
for i in range(size_of_ls):
    if len(tmp) < len(ls1[i]):
        tmp = ls1[i]
        index = i


print(f"The longest string is: {ls1[index]}\n"
      f"The index of the longest string is: {index}\n")


print("Հայտարարել list,  որը բաղկացած է string-ներից:\n"
      "List-ում եղած բոլոր string-ների առաջին տառը դարձնել մեծատառ:\n"
      "Տպել յուրաքանչյուրի առաջին տառը:\n")
ls2 = ["person", "book", "student", "car", "hairs"]
print(ls2)

for i in ls2:
    i = i[0].upper() + i[1: ]
    print(i[0])

print("\nՀայտարարել list և տպել list-ի էլեմենտները  հակառակ հերթականությամբ:\n"
      "List-ը կարող է պարունակել ցանկացած տիպի էլեմենտ:\n")
ls3 = ["start", 86, "class", 4.54, "phone", "table", 13, "end"]
print(ls3)

i = len(ls3) - 1
while i >= 0:
    print(ls3[i])
    i -= 1


print("\nԳրել ծրագիր, որը ստանում է ամբողջ թիվ։ Հայտարարել list:\n"
      "Եթե list-ում առկա է տրված թիվը տպել YES, հակառակ դեպքում տպել NO։")
num = int(input("Enter a number: "))
ls4 = [12, 23, 34, 45, 56, 67, 78, 89, 90]
print(ls4)

indicator = False
ind = len(ls4) - 1
for i in range(ind):
    if num == ls4[i]:
        indicator = True
        ind = i
        break
if indicator:
    print(f"Yes, index is {ind}")
else:
    print("No")


# Գրեք ծրագիր, որը ամբողջ թվային զանգվածի բոլոր զույգ էլեմենտները կտեղավորի նույն զանգվածի մեջ սկզբից, իսկ կենտերը՝ վերջից:


ls5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(ls5)
size = 0
ls_tmp1 = []
ls_tmp2 = []
for i in range(len(ls5)):
    if ls5[i] % 2 != 0:
        ls_tmp1.append(ls5[i])
    else:
        ls_tmp2.append(ls5[i])
ls5 = ls_tmp2 + ls_tmp1
del ls_tmp1
del ls_tmp2
print(ls5)

