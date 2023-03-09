# favorite_sports = ["football", "baseball","tennis","pingpong"]

# dictionary
# دیکشنری

# favorite_sports = {}
# print(type(favorite_sports))
# دیکشنری ساختار کلید و مقدار دارد
# جفت کلید و مقدار
favorite_sports = {
    'sara': 'football',
    'tina': 'tennis',
    'reza': 'baseball',
    'artin': 'football'
}

print(favorite_sports['artin'])
# print("sara likes", favorite_sports['sara'])

# favorite_sports = {
#     0: 'football',
#     1: 'tennis',
#     2: 'baseball',
#     3: 'football'
# }
# print(favorite_sports[0])

favorite_sports["rozha"] = "basketball"
print(favorite_sports)

del favorite_sports['reza']
print(favorite_sports)


# exercise 1 :
# نام، نام خانوادگی، سن و نام پدر یک دانش آموز را از ورودی دریافت نمایید
# و در دیکشنری ذخیره نمائید
# اطلاعات دیکشنری را پرینت کنید.
students = {}
students['name'] = "ali"
students['family'] = "rezaei"
