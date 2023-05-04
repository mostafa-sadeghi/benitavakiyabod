# for number in [1,5,0,-1,100]:
#     print(number, end=' ')

# for char in 'python':
#     print(char.upper(), end=' ')
# exe1:
# برنامه ای بنویسید که لیستی از اعداد زیر بسازد و سپس مجموع آنها را محاسبه و نمایش دهد
# 3 4 7 -1 0 9 99 103
# with for loop

# total = 0
# for num in range(1000,1_000_001):
#     total = total + num

# print(total)


# for i in range(3):
#     print("a")


# total = 0
# for i in range(5):
#     n = int(input('enter a number: '))
#     total = total + n

# print(total)
##################################################
# total = 0
# i = 0

# while i < 5:
#     n = int(input('enter a number: '))
#     total += n
#     i += 1

# print("total is :", total)

# print(5 % 2)

#  برنامه ای بنویسید که پنج عدد از وروید دریافت نماید و حاصلجمع اعداد 
# زوج وارد شده را پر ینت کند

total = 0
for i in range(5):
    n = int(input('enter a number: '))
    if n % 2 == 0:
        total += n

print("sum of even number : ", total)

# برنامه بالا را با حلقه وایل انجام دهید

