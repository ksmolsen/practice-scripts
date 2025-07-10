"""This is not a single script, but a collection of different snippets of code aimed at
refreshing and reinforcing my list, tuple, dict syntax, among other things. The goal is to 
make my vocabulary accurate"""

#Run this in terminal: this method makes a string upper case. Strings are immutable, so the string that is printed is a new string.
"hello".upper()

#Run this in terminal: This method replaces the first value with the second one. Strings are immutable, so the string that is printed is a new string.
"hello".replace("h", "j")

#Repeating basic list syntax.
list_example = []
dict_example = {}
tuple_example = ()

list_example = ["item 0", "item 1", "item 2"]

print(list_example)

#Append add an item to the end of the list.
list_example.append("item 3")

print(list_example)

#A list can store any data type, like the int and float in the examples below.
list_example.append(701)
list_example.append(19.99)

print(list_example)

#Strings, lists and tuples are iterable objects, meaning the items stored in them can be accessed in a loop.
#Each item in an iterable object has an index representing the position of the item, starting with position 0, not 1.

#Access the item by using the index number in [].
print(list_example[0])
print(list_example[3])
print(list_example[4])

#An exception will be raised if you try to access an index out of range.

#Lists are mutable, meaning you can change the items stored in them.

list_example[1] = "Updated item"

print(list_example)

#The pop method removes the last item from a list and return it. In this example, it should remove the float 19.99.

list_example.pop()

print(list_example)

#You can not use pop on an empty list. If you do Python will raise an exception. This is called an IndexError.

#You can pop an item at a specific index by specifying the index inside the ().
list_example.pop(0)

print(list_example)

#You can combine two lists. Just use a +. This is called to concatenate.

list_example_2 = ["list 2 item"]

combined_list = list_example + list_example_2

print(combined_list)

#You can check if an item is in a list. Item in list is the way to do it. Use not to get False bool.

print(701 in combined_list)
print(701 not in combined_list)

#You can check the number of items in a list with len. 

print(len(combined_list))

#Tuples are immutable, meaning that once they are created, they can not be changed.

tuple_example = ()

#Use commas to separate items in a tuple. 

tuple_example = (10, 20, 30, 40, 50,)

#Tuples holding only a single item must end with a comma for Python to understand it's a tuple. This is true regardless of type.

tuple_or_string = ("Add a comma",)

print(tuple_or_string)

#If you try to change a tuple Python will raise an exception.

#You can get an item from a tuple the same way as from a list, by referencing its index.

print(tuple_example[1])

#You can check if an item is in a tuple with the keyword in. Returns a bool. Use the keyword not to get a bool False.

if 20 in tuple_example:
    print(tuple_example[3])
else:
    print("20 not in tuple_example")    
    
if 30 not in tuple_example:
    print("30 not in tuple_example")
else:
    print(tuple_example[4])

#Tuples can be used in situations where the data must not be changed, as tuples are immutable. Tuples are also faster than lists as they take up less memory.












