students = {"Alex": 10, "Peter": 9,
            "Victor": 7, "Anna": 8,
            "Kate": 8, "Vladimir": 10,
            "Nikita": 8}



print("Before:", students)
del students["Victor"]                 # Удаление элемента
print("After:", students)

print("Before:", students)
students.pop("Anna")                 # Удаление элемента
print("After:", students)

print("Before:", students)
students.popitem()               # Удаление  последнего элемента
print("After:", students)

print("Before:", students)
students.clear()                    # Очищение списка(удаление всех элементов)
print("After:", students)
