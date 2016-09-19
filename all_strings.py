""" Calculates all possible combinations of strings given an input of characters
and the length of the combinations desired.
E.g. print(sorted(all_strings({'a', 'b','c'}, 1))) -> ['a', 'b', 'c']
print(sorted(all_strings({'a', 'b','c'}, 3))) -> ['aaa', 'aab', 'aac', 'aba'...
Written by Daniel Lynch
"""

def all_strings(alpha, length):
    lst = []
    if length == 0:
        return lst
    mylist = list(alpha)
    newlist = []
    for i in mylist:
        newlist.append(str(i))
        lst.append(str(i))
    while length > 1:
        lst = add_one(lst, newlist)
        length -= 1
    return lst
        
def add_one(current_list, alpha):
    output = []
    for i in current_list:
        for j in alpha:
            output.append(i+j)     
    return output
            
print(sorted(all_strings({'a', 'b','c'}, 3)))