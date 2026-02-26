names = ["Melina","Erjon","Egzoni","Andi"]

for name in names:
    print(name)




sentence = "Hello world"

for character in sentence:
     if character.isalpha():
         print(character)

for number in range(1,9):
    print(number)

numbers = [23,45,89,90,2,1,45]

maximum =  numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num
        print("the biggest number in this list is :",maximum)

