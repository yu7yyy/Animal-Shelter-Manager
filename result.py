def add_animal(animals, name, age, weight):
    animal = {
        "name": name,
        "age": age,
        "weight": weight
    }

    animals.append(animal)
    print("Animal added")


def show_animals(animals):
    if not animals:
        print("No animals in shelter")
        return

    for a in animals:
        print(a["name"], a["age"], a["weight"])
