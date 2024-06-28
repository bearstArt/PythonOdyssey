print("Task 1")
print("Write a program that searches through the string “find the letter z”\n" 
      "and prints the index of the first occurrence of ‘z’.\n" 
      "If ‘z’ is not found, print “Character not found”.\n")


def find_the_letter_z(input_text):
    for t in range(len(input_text)):
        if input_text[t] == "z" or input_text[t] == "Z":
            print(t)
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
