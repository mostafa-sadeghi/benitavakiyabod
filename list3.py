numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# numbers.append(100)
# print("my list items:", numbers)

# print("we want to delete last item:")
# del numbers[9]
# print("my list items:", numbers)

# del numbers[-1]
# print("my list items:", numbers)

# print("we want to remove number 4 from the list")
# numbers.remove(4)
# print("my list items:", numbers)

# print("we want to print our list reversely")
# print(numbers[-1::-1])
# del numbers[0]
# del numbers[-1:0:-1]
# print(numbers)

# del numbers[-1:-4:-1]
# print(numbers)
# exericse 1:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# برنامه ای بنویسید که مجموع اعداد زوج لیست بالا را پرینت نماید
# برنامه ای  بنویسید که مجموع اعداد فرد لیست بالا را پرینت نماید

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# even_numbers = numbers[1::2]
# print("even numbers are:", even_numbers)
# print("sum of even numbers is:", sum(even_numbers))
# print()

# odd_numbers = numbers[::2]
# print("odd numbers are:", odd_numbers)
# print("sum of even numbers is:", sum(odd_numbers))

# str1 = "ali"
# str2 = "sima"

# output = str1 + str2
# print(output)


# my_list1 = [1, 2, 3, 4, 5, 'a', 'b', 'c']
# my_list2 = ["ali", "reza"]
# output = my_list1 + my_list2
# print(output)

another_list = [1, 2, 3, [4, 5]]
# print(another_list[0])
# print(another_list[1])
# print(another_list[2])
# print(another_list[3])
# print("we want to print number 4 and number 5")

# print(another_list[3][0])
# print(another_list[3][1])

# exercise 2   برنامه ای بنویسید که حاصل جمع اعداد موجود در لیست زیر ر امحاسبه نماید و پرینت کند
# somrthing = [1, 2, 3, [2, 2], [3, 6, 8]]
something = [1, 2, 3, [2, 2], [3, 6, 8]]
result = something[0] + something[1] + something[2] + something[3][0] + \
    something[3][1] + something[4][0] + something[4][1] + something[4][2]
print("sum of all numbers in the list is equal to:", result)

result = something[0] + something[1] + something[2] + \
    sum(something[3]) + sum(something[4])
print("sum of all numbers in the list is equal to:", result)

# str1 = '@'
# print(str1 * 6)

# list1 = ['a', 'b', 'c']
# print(list1 * 8)
