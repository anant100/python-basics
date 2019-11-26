

# Keyworded Variable Length agruments are defined with double star **


def person(name, **data):
    print(name)

    for i,j in data.items():
        print(i,j)


person("Anant", Age=23, City="Montreal", Mobile=+1482657392)
