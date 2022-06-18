class Stack:
    def __init__(self):
        data=[]
        self.data = data

    def push(self,obj):
        self.data.append(obj)

    def pop(self):
        self.data.pop(-1)

    def dispay(self):
        print(self.data)

print("---- Stack Implementation ---- \n\n")

def __display():
    print("\n\t\tEnter your choice:\n")
    print("\t\t1: Push\n")
    print("\t\t2: Pop\n")
    print("\t\t3: Display\n")
    print("\t\t0: Exit")
__display()
choice = int(input())

new_object=Stack() 
while choice:
    if choice==1:
        n = int(input("Enter number: \n"))      
        new_object.push(n)
        __display()
        choice = int(input())
    elif choice==2:
        new_object.pop()
        __display()
        choice = int(input())
    elif choice==3:
        new_object.dispay()
        __display()
        choice = int(input())
    else:
        print("Wrong choice try again: \n")
        break