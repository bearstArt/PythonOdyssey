import Decor

print("Task 1\n")
print("Write a program that inserts a value at a specified index in a list without using the built-in insert() method.\n"
      " For example, insert the value 3 at index 1 in the list [1, 2, 4, 5] to make it [1, 3, 2, 4, 5].")

size_list = int(input("Enter the size of the list: "))
ls1 = ([0] * size_list) if size_list > 0 else print("Size of the list is not a positive number\n")
print(ls1)
for i in range(size_list):
    ls1[i] = input(f"Enter the value for the index {i} of the list: ")



index = int(input("Enter the index to insert the value: "))
ls2 = [0]
ls2[0] = input("Enter the value to insert: ")

def ins(list1, list2, index):
    if index < 0:
        print("Index cannot be negative")
        return
    elif index > len(list1):
        print("Index out of range")
        return
    elif index == 0:
        return list(list2) + list1
    else:
        return list1[:index] + list(list2) + list1[index:]


ls = ins(ls1, ls2, index)
print(ls)
print("================================\n")


print("Task 2\n")
print("Write a program that removes the first occurrence of a specified element from a list without using the remove()\n"
      " method. If the element does not exist, print a message.\n"
      " Example: Remove 2 from [1, 2, 3, 2, 4] resulting in [1, 3, 2, 4].")

def rem(list, element):
    for i in range(len(list)):
        if list[i] == element:
            return list[:i] + list[i + 1:] if i > 0 else list[i + 1:]

element = input("Enter the element to remove: ")
print(rem(ls, element))
