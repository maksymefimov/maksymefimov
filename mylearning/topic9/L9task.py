salaries = { "John": 15000, "Ann": 30000, "Mike": 12000, "Mary": 15000 }
print(salaries)
print(type(salaries))
## [] is used to return the value associated with key!!!
print()
print("Ann`s salary is",salaries["Ann"])
##Note that the dictionary is not a sequence-type container like a list.
##Even though the subscript operator is used with a dictionary, you cannot access the items by
##index or position.
##A value can only be accessed using its associated key
##The key supplied to the subscript operator must be a valid key in the dictionary or a KeyError
##exception will be raised.
##To find out whether a key is present in the dictionary, use the in (or not in) operator:
print()
key_name = input("Input the name: ")
if key_name in salaries:
    print("%s salary is %s"%(key_name,salaries[key_name]))
else:
    print("%s salary is not in my list"%key_name)
##Default Value
print()
number = salaries.get("Mike",17000)
print("Salaries: "+ str(number))
print("Salaries: ",salaries)
##Adding and Modifying Items
print()
salaries["Mike"] = 150000
print("Salaries: ",salaries)
##Another Way To Create A Dictionary
##Sometimes you may not know which items will be contained in the dictionary when it’s created.
##You can create an empty dictionary like this:
##and add new items as needed:
print()
salaries = {}
print("Salaries: ",salaries)
salaries["Halyna"] = 1500000
salaries["Max"] = 10000
salaries["Maryna"] = 15000
salaries["Slava"] = 20000
print("Salaries: ",salaries)
##Removing Items
##To remove an item from a dictionary, call the pop() method with the key as the argument:
print()
salaries.pop("Slava")
print("Salaries: ",salaries)
##Traversing a Dictionary
##•You can iterate over the individual keys in a dictionary using a for loop:
print()
for key in salaries:
    print(key)


        
    

