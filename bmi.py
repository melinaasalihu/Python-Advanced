from abc import ABC, abstractmethod

# Abstract base class
class Person(ABC):
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self._weight = weight
        self._height = height

    # Encapsulation using property
    @property
    def weight(self):
        return self._weight

    @property
    def height(self):
        return self._height

    @abstractmethod
    def calculate_bmi(self):
        pass

    @abstractmethod
    def get_bmi_category(self, bmi):
        pass

    def print_info(self):
        bmi = self.calculate_bmi()
        category = self.get_bmi_category(bmi)
        print(f"\nName: {self.name}")
        print(f"Age: {self.age}")
        print(f"BMI: {bmi:.2f}")
        print(f"Category: {category}")


# Adult class
class Adult(Person):
    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def get_bmi_category(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 24.9:
            return "Normal weight"
        elif bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"


# Child class
class Child(Person):
    def calculate_bmi(self):
        return (self.weight / (self.height ** 2)) * 1.3

    def get_bmi_category(self, bmi):
        if bmi < 14:
            return "Underweight"
        elif bmi < 18:
            return "Normal weight"
        elif bmi < 24:
            return "Overweight"
        else:
            return "Obese"


# BMI Application class
class BMIApp:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def collect_user_data(self):
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        weight = float(input("Enter weight (kg): "))
        height = float(input("Enter height (m): "))

        if age >= 18:
            person = Adult(name, age, weight, height)
        else:
            person = Child(name, age, weight, height)

        self.add_person(person)

    def print_results(self):
        print("\n--- BMI Results ---")
        for person in self.people:
            person.print_info()

    def run(self):
        while True:
            self.collect_user_data()
            choice = input("\nAdd another person? (yes/no): ").lower()
            if choice != "yes":
                break

        self.print_results()


# Run the app
if __name__ == "__main__":
    app = BMIApp()
    app.run()