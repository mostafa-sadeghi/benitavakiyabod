# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(numbers[0:9:2])
# print(numbers[1:9:2])

# print(numbers[:3])

# print(sum(numbers))

# چهار عدد را از ورودی بگیرید و در لیستی اضافه کنید و سپس مجموع اعدا لیست را نمایش دهید.
# یک برش از ابتدا تا دومین عدد لیست ایجاد نمائید.
n1 = int(input('enter first number: '))
n2 = int(input('enter second number: '))
n3 = int(input('enter third number: '))
n4 = int(input('enter forth number: '))

numbers = []
numbers.append(n1)
numbers.append(n2)
numbers.append(n3)
numbers.append(n4)
print("sum of all numbers is:", sum(numbers))
