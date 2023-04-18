students = {"Alex": 10, "Peter": 9, "Victor": 7,
            "Anna": 8, "Kate": 8, "Vladimir": 10,
            "Nikita": 8}

# print(len(students))

# for element in students:
#     print(element)
#
# for element in students.keys():  # Перебирает ключи
#     print(element)
#
#
# for element in students.values():  # Перебирает значения
#     print(element)

# for key in students:  # Перебирает ключи и значения
#     print(key + " - " + str(students[key]))


for item in students.items():
    print(item)                # Способы вывода данных
х

for key, value in students.items():
    print(key, "-", value)              # Способы вывода данных
