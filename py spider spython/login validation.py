#Login validation
def login(user_name, password):
    if user_name in credentials:
        actual_password=credentials[user_name]
        if password==actual_password:
            print("Login Successful")
            print(user_name)
        else:
            print("Password is wrong")
    else:
        print("User name  not existing")
def get_credentials():
    global user_name
    global password
    user_name=input("Enter user name :")
    password=input("Enter user Password :")
   

credentials={"dinesh":"123@123","chinky":"yk@ky","dhanush":"Diament","pankaj":"@123"}


n=1

while n:
    print(1,"signup")
    print(2,"login")
    print(3,"exit")
    choice=int(input("Enter your choice :"))
    match choice:
        case 1:
            get_credentials()
            correct_password=input("Enter user Password again:") 
            n=1
            if password==correct_password:
                credentials.update({user_name:password})
                print("signup successful")
                login(user_name, password)
            else:
                print("Password is wrong")
    
        case 2:
            get_credentials()
            login(user_name, password)        
        case 3:
            n=0
            exit
        case _:
            print("Wrong choice")
print("Thank you")





