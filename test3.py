
age = int(input("Input vik:"))

if age > 0 and age < 18:
    print("Yuo are less 18")
elif age > 18 and age < 25:
   print("You are between 18 and 25")
elif age > 25 and age < 50:
    print("You are between 25 and 50")
else:
    print("You are more than 50")