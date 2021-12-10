from execute import *

menu_options = {
    1: 'Create Model',
    2: 'Upload Data',
    3: 'Make querys',
    4: 'Delete Model',
    5: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def option1():
     createModel()

def option2():
     uploadDate()

def option3():
     querysMake()

def option4():
     deleteModel()

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            option4()
        elif option == 5:
            print('Thanks for use this app')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')