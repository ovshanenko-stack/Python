#Ask user to input number
num = int(input("Ведіть число: "))
#Check if number is positive, negative or zero
if num % 2 == 0:
    print(f"Число {num} є парним")
else:
    print(f"Число {num} не є парним")
