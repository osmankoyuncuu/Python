# Write a Python program that;
# Takes a positive integer number from the user,
# Checks the entered number if it is Armstrong,
# consider the negative, float and any entries other than numeric values then display a warning message to the user.
number = input("Entered a positive integer number: ")
if number.isdigit() == True and int(number) > 0 :
    x = len(number)
    total = 0
    for i in number:
        total += int(i) ** x
    if total == int(number):
        print(f"{number} is an Armstrong number")
    else:
        print(f"{number} is not an Armstrong number")
else:
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
