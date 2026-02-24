from lesson1.variables import temperature

age = 18

if age >= 18:
    print("you can vote")
else:
    print("you cannot  vote yet.")

temperature = 28

if temperature > 30 :
    print("its hot day,stay hydrated")
elif 20  <= temperature <=30:
    print("the weather is pleasant")
else:
    print("its a cold day")


number = 7

if number % 2 == 0:
    print("the number is even")
else:
    print('the number is odd')