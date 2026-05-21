#Secret password
password = 135796

#Create a 3 attempts
attempts = 3
print("У вас є 3 спроби ввести коректний пароль.")

#After 3 attempts you will be blocked
while attempts > 0:
    user_input = input("Введіть пароль: ")
    if user_input == str(password):
        print("Ви ввели правильний пароль. Вітаємо!")
        break
    else:
        attempts -= 1
        print(f"Невірний пароль. У вас залишилось {attempts} спроб.")

if attempts == 0:
    print("Ви використали всі спроби. Спробуйте пізніше.")
