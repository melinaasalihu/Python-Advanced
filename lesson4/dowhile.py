while True:
    user_input= "please enter a positive  number"

    if user_input.isnumeric():
        number = int(user_input)

        if number > 0:
         break

    print ("invalid input. Please try again")

print("you entered a valid positive number which is:",number)
