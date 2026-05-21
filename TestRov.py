#Ask user to input number
#num = int(input("Ведіть число: "))
name = [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
#Check if number is positive, negative or zero
max = name[0]
min = name[0]
for i in name:
    if i > max:
        max = i

    elif i < min:
        min = i
print(f"Максимальне число: {max}")
print(f"Мінімальне чиcло : {min}")

