# list names, indexy, type(), len(), append()

names = ["Petr","Alena","Josef","Monika"]

print(names)
print(names[0])
print(names[-1])

print(type(names))
print(len(names))

names[1] = "Stanislava"
names[-2] = names[0]
print(names)

names.append("Miroslav")
print(names)


# list numbers, f-string, vytvoření z listu names a numbers nový list names_and_numbers

numbers = range(1,101,2)

numbers = list(numbers)
print(numbers)
print(f"{names[0]} se umístil jako {numbers[0]}. v pořadí.")

names_and_numbers = names + numbers
print(names_and_numbers)


# nové listy list_of_numbers, another_list_of_numbers, next list (vytvoření kopie)

list_of_numbers = [0,1,2,3,4,5,6,7,8,9,10]
print(list_of_numbers)

another_list_of_numbers = list_of_numbers + [11,12,13,14,15]
print(another_list_of_numbers)

print(another_list_of_numbers[2:6])
next_list = another_list_of_numbers[:]
print(next_list)


# for cykly

for number in list_of_numbers:
    print(number)

for index, name in enumerate(names):
    print(f"index: {index} - name: {name}")


# zip()

books = ["Book 1", "Book 2", "Book 3", "Book 4"]
price = [499,249,599,349]

for item, amount in zip(books, price):
    print(f"Kniha {item} stojí: {amount} Kč.")


# in, not in

print("Book 2" in books)
print("Book 3" not in books)


a,b,c = "Item 1", "Item 2", "Item 3"
a,b,c = c,b,a
print(a)
print(c)


# append(), insert()

books.append("Book 5")
print(books)

books.insert(2,"Časopis")
print(books)


# del(), remove()

del books[-1]
print(books)

books.remove("Časopis")
print(books)


# pop(), sort()

books.pop()
print(books)

books.pop(1)
print(books)


numbers2 = [-18,27,0,-7,117,2]
numbers2_list = list(numbers2)

numbers2_list.sort()
print(numbers2_list)

names.sort()
print(names)


# tuple, list

names2 = ("Lenka", "Milan", "Aneta", "Filip")
print(names2[1])

names2[:]
print(names2)


my_tuple = tuple(names)
print(my_tuple)

tuple1 = (1,2,3,4,5)
my_list = list(tuple1)
print(my_list)