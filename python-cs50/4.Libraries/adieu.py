import inflect

p = inflect.engine()
names = []

while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        break

mylist = p.join((names))
print("Adieu, adieu, to", mylist)

