"""
method list
 menu
# load
# add
# print
# delete
# search
"""

# from helper_gen import menu
from enum import Enum
from helper_ar import add, print_all,delete, search
from helper_file import load,save

contacts=[]
DATA_FILE='my_contacts.json'
# implemented

class MyMenu(Enum):
    ADD =2
    PRINT =3
    DELETE = 4
    SEARCH =5
    EXIT =6

# display menu, get user selection
def menu():
    for opt in MyMenu:
        print(f"{opt.value} - {opt.name}")

    user_selection=input("your selection:")
    return int(user_selection)




def main():
    contacts=load(DATA_FILE) # load from file to contacts list
    user_selection= menu() # get user selection from menu 
    while  user_selection != MyMenu.EXIT.value:
        if user_selection == MyMenu.ADD.value :add(contacts) # add new contact to contacts
        if user_selection == MyMenu.PRINT.value :print_all(contacts) #print all contacts
        if user_selection == MyMenu.DELETE.value :delete(contacts) # delete a contact
        if user_selection == MyMenu.SEARCH.value:search(contacts) # search a contact
        user_selection= menu()
    save(DATA_FILE,contacts) # save all contacts to JSON file

if __name__ == "__main__":
    main()