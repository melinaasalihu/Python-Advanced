try:
    result = 10 / 0
except ZeroDivisionError:
    print("Oops! Tried to divide by zero")

fruits = {
    "strawberries": 5,
    "cherries": 7,
    "orange": 3
}
try:
   print(fruits["apple"])

except KeyError:
    print("the key does not exist in the directory")


text = "this is not a number"

try:
    text_to_int = int(text)

except Exception as e:
    print("An error occurred while parsing data", e)

try:
    result = 10 / 2
except ZeroDivisionError:
    print("Division by zero error occurred")
else:
    print("Division successful. Result:", result)


try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("finally block executed")



def devide_numbers(a,b):
    try:
        result = a / b
        print("result of division",result)
    except ZeroDivisionError:
        print("Invalid division by zero")
    except TypeError:
        print("invalid type for division")
    except Exception as e:
        print(f"unexpected error {e}")

devide_numbers(10,2)
devide_numbers(10,0)
devide_numbers(10, '2')