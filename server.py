from result import add_animal, show_animals

animals = []

while True:
    print("\nAnimal Shelter Manager")
    print("1 - Add animal")
    print("2 - Show animals")
    print("3 - Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        age = int(input("Age: "))
        weight = float(input("Weight: "))
        add_animal(animals, name, age, weight)

    elif choice == "2":
        show_animals(animals)

    elif choice == "3":
        break
