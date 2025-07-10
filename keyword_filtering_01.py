"""Practice script. A dict with author, year and title of books. Task: filter keywords in a dict by value."""

#Dict key words can only hold one value, but that value can be a list. 
books_dict: dict[str, tuple[str, int]] = {"title_a": ("Author A", 1970), "title_b": ("Author B", 1980), "Title c": ("Author C", 1990)}


def value_filter():
    for key, value_tuple in books_dict.items():
        if value_tuple[1] > 1975:
            print(key)
        
value_filter()        
        
#Notes to self:

#Dict key words can only hold one value, but the value an be a list or tuple.

#value_tuple can also be value_list if a list is used

#.items() is a method that runs through both keys and values simulaneously

#value_tuple[1], remember that python start counting positions at [0]

#Tuples are lighter than lists as they only take up one place in memory, lists more than one as they need to be able to be changed.