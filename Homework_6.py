import Decor
print("Task 1")
print("Write a program that searches through the string “find the letter z”\n" 
      "and prints the index of the first occurrence of ‘z’.\n" 
      "If ‘z’ is not found, print “Character not found”.\n")


def find_the_letter_z(input_text):
    for t in range(len(input_text)):
        if input_text[t] == "z" or input_text[t] == "Z":
            print(f"The index of letter 'z' is: {t}")
            break
        if t == len(input_text) - 1:
            print("\nCharacter 'z' not found\n")


text = input("Enter string: ")
find_the_letter_z(text)
print("================================\n")


print("Task 2\n")
print("Given the string “capitalize”, transform the first character \n"
      "to uppercase to make it “Capitalize” (use ASCII table). Hint\n" 
      "(the difference between the ASCII values of a lowercase letter and\n" 
      "its corresponding uppercase letter is 32. Specifically, to convert a\n" 
      "lowercase letter to uppercase, you subtract 32 from its ASCII value.)\n")

@Decor.debug(enabled=True)
def capitalize(word):
    if ord("a") <= ord(word[0]) <= ord("z"):
        word = chr(ord(word[0]) - 32) + word[1:]
    for w in range(1, len(word)):
        if ord("A") <= ord(word[w]) <= ord("Z"):
            word = word[:w] + chr(ord(word[w]) + 32) + word[w + 1:]
    
    return word


text = capitalize(text)
print(f"Capitalized string is: '{text}'")
print("================================\n")


print("Task 3")
print("Convert the string “hello, world! are you ready?” into title case,\n"
      "where each word starts with an uppercase letter, resulting in\n"
      "“Hello, World! Are You Ready?“. (use ASCII table)\n")

text = "hello, world! are you ready?"
new_text = ""
if ord("a") <= ord(text[0]) <= ord("z"):
    new_text = chr(ord(text[0]) - 32)
for i in range(1, len(text)):
    if text[i - 1] == " ":
        if ord("a") <= ord(text[i]) <= ord("z"):
            new_text = new_text + chr(ord(text[i]) - 32)
    else:
        new_text = new_text + text[i]

text = new_text
del new_text
print(text)
print("================================\n")


print("Task 4\n")
print("Create a program that reverses the string “reverse me” and prints “em esrever”.")
text = "reverse me"
text = text[- 1 ::-1 ]
print(text)
print("================================\n")


print("Task 5\n")
print("Write a program that checks if the string “radar” is a palindrome (reads the same forward and backward)\n"
      " and print “Yes” if it is, or “No” if it is not.\n")
text = "radar"
if text == text[-1::-1]:
    print("Yes, it's a palindrome")
else:
    print("No, this is not a palindrome")
print("================================\n")


print("Task 6\n")
print("Given two strings, “hello” and “world”, write a program to concatenate them with a space in between,\n"
      " resulting in “hello world”.\n")
st1 = "Hello"
st2 = "world"
st3 = st1 + ", " + st2 + "!"
st4 = (f"{st1}, {st2}!")
print(st3)
print(st4)
print("================================\n")


print("Task 6\n")
print("Write a program that replaces every occurrence of the letter ‘a’ with ‘x’\n"
      " in the string “banana” and prints “bxnxnx”.")
fruit = "banana"
tmp = ""
for i in range(len(fruit)):
    if fruit[i] == "a":
        tmp = (f"{fruit[:i]}x{fruit[i+1:]}")
        fruit = tmp
del tmp
print(fruit)