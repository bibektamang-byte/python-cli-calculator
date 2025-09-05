# CLI calculator

# input taker:
def take_input(prompt="Enter number: "):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Invalid input! Please enter a valid number.")
# -------------------- fucntions ---------------------------
def add():
    a = take_input()
    b = take_input()
    print(f"The sum is {a+b}.")

def subtract():
    a = take_input()
    b = take_input()
    print(f"The difference is {a-b}.")

def multiply():
    a = take_input()
    b = take_input()
    print(f"The product is {a*b}.")     

def division():
    while True:
        a = take_input()
        b = take_input()
        try:
            print(f"The division is {a/b:.2f}.")
        except ZeroDivisionError:
            print("Number cannot be divided by 0.")
            print("Try Agian!")
            print("-"*50)
            continue
        break

def square():
    a = take_input()
    print(f"The square of {a} is {a**2}.")          
        
# ------------------------operations------------------------
choices = {
    "1":"Addition",
    "2":"Subtraction",
    "3":"Multiplication",
    "4":"Division",
    "5":"Square"
}

# ------------------Choosing the operation------------------
print("="*50)
print("WELCOME TO PYTHON CALCULATOR".center(50))
print("="*50)
for key,choice in choices.items():
    print(f"{key}. {choice}")
print("-"*50)
  
while True:
    choose = input("enter your choice('q' to quit): ")
    print("-"*50)
    if choose in choices.keys():
        if choose == "1":
            add()
            print("-"*50)
        elif choose == "2":
            subtract()
            print("-"*50)
        elif choose == "3":
            multiply()
            print("-"*50)
        elif choose == "4":
            division()
            print("-"*50)
        else:
            square()
            print("-"*50)
            
    elif choose in ["quit","q"]:
        print('EXITED...')
        break
    else:
        print("Invalid choice, try agian!")
        continue
print("="*50)




    

             
    
    
    