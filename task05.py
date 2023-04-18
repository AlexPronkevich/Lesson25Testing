students = {"Alex": 10, "Peter": 9,
            "Victor": 7, "Anna": 8,
            "Kate": 8, "Vladimir": 10,
            "Nikita": 8}

print("Before:", students)
students["Alice"] = 5
print("After:", students)


print("Before:", students)
students["Anna"] = 6
print("After:", students)

print("Before:", students)
students.setdefault("Ivan", 10)
print("After:", students)

print("Before:", students)
students.update({"Denis" : 10, "Vova" : 7})
print("After:", students)