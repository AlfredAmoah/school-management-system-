from tkinter import *
root = Tk()
mylabel = Label(root, text = 'welcome To KNUST Portal')
mylabel = Label(root, text = 'Choose From The Options Below')
mylabel.grid(row = 0, column= 1)
mylabel.grid(row = 1, column= 2)


import json
def ask():
    name = input('name: ')
    reference = input('reference: ')
    index = input('index: ')
    insert(name, reference, index)
    

def insert(name, reference, index):
    

    data = {
        "name": name,
        "refrence": reference,
        "index": index
    }
        
    with open('app.json','r') as f:
        students = json.load(f)
        for student in students:
            if student['refrence'] == data['refrence']:
                print('Student already exist')
                break
        else:
            students.append(data) 

    with open('app.json', 'w') as f:
        json.dump(students, f, indent=3)

def search():
    search_key = input('Enter students reference number to search: ')
    with open('app.json','r') as f:
        students = json.load(f)
    for student in students:
        if student['refrence'] == search_key:
            print(student)
            break
        
    else:
        print("User does not exist")
    


def main():
    print('Welcome to KNUST Admission Portal\n')
    print('Choose one of the options below\n')
    print('1. Insert \n')
    print('2. Search \n')
    option = int(input('Choose 1 or 2\n'))
    while(option != 1 and option != 2):
        print('Invalid input\n')
        option = int(input('Please enter 1 or 2\n'))

    if option == 1:
        ask()
    if option == 2:
        search()

main()
mybutton1= Button(root, text = 'add student', command= ask)
mybutton2 = Button(root, text = 'search for student', command = search)
mybutton1.grid(row = 0, column= 1)
mybutton2.grid(row = 1, column =1,)


e1 = Entry(root,  text = 'name',width= 10)
e2= Entry(root, text = 'reference No', width= 5)
e3 = Entry(root, text = 'index No', width= 5)
e1.grid(row = 0, column =1 )
e2.grid(row = 1, column = 1)
e3.grid(row = 2, column = 1)

mybutton = Button(root, text ='Enter', command = insert )

e4 = Entry(root, text = 'Enter the student you want to search')

mybutton = Button(root, text = 'Enter', command = search)
 
mylabel = Label(root, text = 'please thank you for using the portal')

root.mainloop()