"""This is not a single script, but a collection of different training snippets, aimed at r
efreshing and reinforcing my list, tuple, dict syntax, among other things."""

#Run in terminal: this method makes the string upper case and prints it.
"hello".upper()

#Run in terminal: This method replaces the first value with the secons and prints it.
"hello".replace("h", "j")

#Repeating basic list syntax
list_example = []
dict_example = []
tuple_example = ()

list_example = ["item 0", "item 1", "item 2"]

print(list_example)

#append add an item to the end of the list
list_example.append("item 3")

print(list_example)

#A list can store any data type
list_example.append(701)
list_example.append(19.99)

print(list_example)

#Strings, lists and tuples are iterable objects, meaning the items stored in them can be accessed in a loop.
#Each item in in an iterable object has an index representing the position of the item, starting with position 0, not 1.

#Access the item by using the index number in [].
print(list_example[0])
print(list_example[3])
print(list_example[4])

#An exception will be raised if you try to acces an index out of range.

#Lists are mutable, meaning you can change the items stored in them.

list_example[1] = "Updated item"

print(list_example)




