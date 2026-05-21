#Ask user to input number
num = int(input("Введіть число для таблиці множення: "))

print(f"Таблиця множення для числа {num}:")

#Generate multiplication table from 1 to 10
for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")