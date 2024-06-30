my_list = [1, 2, 3]
print("Initial list:", my_list)

my_list.append(4)
print("List after adding an element:", my_list)

my_list.remove(2)
print("List after removing an element:", my_list)

my_list[0] = 10
print("List after modifying an element:", my_list)


my_dict = {'a': 1, 'b': 2, 'c': 3}
print("\nInitial dictionary:", my_dict)

my_dict['d'] = 4
print("Dictionary after adding a key-value pair:", my_dict)

del my_dict['b']
print("Dictionary after removing a key-value pair:", my_dict)

my_dict['a'] = 10
print("Dictionary after modifying a value:", my_dict)


my_set = {1, 2, 3}
print("\nInitial set:", my_set)

my_set.add(4)
print("Set after adding an element:", my_set)

my_set.remove(2)
print("Set after removing an element:", my_set)

my_set.add(10)  # Modifying a set element by removing and adding a new one
print("Set after modifying an element:", my_set)
