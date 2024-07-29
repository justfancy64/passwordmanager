import os
import filecmp


def main():

    account_check()
    userid = userid_check()
    menu(userid)
    #os.system("steghide embed -ef /root/workspace/github.com/justfancy64/password_manager/test.txt -cf /root/workspace/github.com/justfancy64/password_manager/vault.jpg -sf /root/workspace/github.com/justfancy64/password_manager/vault.jpg -f -p 123")
    #add_password_to_vault()
    #clear_vault()\z




def add_password_to_vault(usrid, path):
        new_data = str(input("enter data for encryption:"))
        #image_path = input("enter existing vault path")
        os.system(f"steghide extract -sf {path} -xf /password_manager/data.txt -f -p {usrid} -q")
        data = open(r"/root/workspace/github.com/justfancy64/password_manager/data.txt", "a")
        data.write(f"\n{new_data}")
        data.close()
        os.system(f"steghide embed -ef /root/workspace/github.com/justfancy64/password_manager/data.txt -cf {path} -sf {path} -f -p {usrid} -q")
        os.system("rm password_manager/data.txt")

def clear_vault(usrid, vault_path):
    os.system(f"steghide extract -sf {vault_path} -xf /root/workspace/github.com/justfancy64/password_manager/data.txt -f -p {usrid} -q")
    open(r"/root/workspace/github.com/justfancy64/password_manager/data.txt", "w").close()
    os.system(f"steghide embed -ef /root/workspace/github.com/justfancy64/password_manager/data.txt -cf {vault_path} -sf {vault_path} -f -p {usrid} -q")
    os.system("rm /root/workspace/github.com/justfancy64/password_manager/data.txt")



def signup():
    os.system("echo creating new user")
    master_username = input("enter your username: ")
    master_password = input("enter your password: ")
    f = open("password_manager/temp.txt", "w")
    f.write(f"{master_username}_{master_password}")
    f.close()
    os.system("steghide embed -ef /root/workspace/github.com/justfancy64/password_manager/temp.txt -cf /root/workspace/github.com/justfancy64/password_manager/template.jpg -sf /root/workspace/github.com/justfancy64/password_manager/usrid.jpg -f -p 123 -q")
    print("please log in using your username and password")
    os.system("rm /root/workspace/github.com/justfancy64/password_manager/temp.txt")

def account_check():
    print("welcome to pogger ogger password manager")
    print("If u have an accoung enter 'y' to log in, otherwise enter 'n'")
    acc_exists = input(":")
    match acc_exists:
        case "y":
            pass
        case "n":
            signup()
        case _:
            print("INVALID INPUT TRY AGAIN")
            account_check()
    
def userid_check():
    
    username = input("enter your username:")
    password = input("enter your password:")
    newid = open("/root/workspace/github.com/justfancy64/password_manager/tempnew.txt", "w")
    newid.write(f"{username}_{password}")
    newid.close()
    os.system("steghide extract -sf /root/workspace/github.com/justfancy64/password_manager/usrid.jpg -xf /root/workspace/github.com/justfancy64/password_manager/temp.txt -p 123 -f -q")
    
    if filecmp.cmp("/root/workspace/github.com/justfancy64/password_manager/temp.txt", "/root/workspace/github.com/justfancy64/password_manager/tempnew.txt"):
        os.system("rm /root/workspace/github.com/justfancy64/password_manager/temp.txt")
        os.system("rm /root/workspace/github.com/justfancy64/password_manager/tempnew.txt")
        return str(f"{username}_{password}")
    
    else: 
        print("wrong credentials")
        userid_check()

def select_template():
    path = input("provide the path of the image u want to use as template")             
    return path

def get_image_vault_path():
    return input("provide the path of your image vault")



def menu(usrid):
    print("       MAIN MENU      ")
    print("Use 'ex' to access an existing vault or 'new' to create a new one")
    print("use 'logout' to change acount")
    command = input(":")
    match command:
        case "ex":
            print("Enter the path to your image")
            path = input(":")
            image_menu(usrid, path)
        case "new":
            create_vault(usrid)
        case "logout":
            account_check()
        case _:
            print("invalid input ")
            menu()


def image_menu(usrid, image_path):
    print("use 'view', 'add', 'clear' or 'change template'")
    command = input()
    match command:
        case "view":
            os.system(f"steghide extract -sf {image_path} -xf /root/workspace/github.com/justfancy64/password_manager/juice.txt -f -p {usrid} -q ")
            f = open("/root/workspace/github.com/justfancy64/password_manager/juice.txt", "r")
            print(f.read())
            f.close()
            os.system("rm password_manager/juice.txt")
            image_menu(usrid, image_path)
        case "add":
            add_password_to_vault(usrid, image_path)
            print('password was saved in the vault')
            image_menu(usrid, image_path)
        case "change template":
            pass
        case "clear":
            clear_vault(usrid, image_path)
            image_menu(usrid, image_path)
        case "back":
            menu(usrid)
        case _:
            print("invalid input")
            image_menu(usrid, image_path)
            

def change_template():
    pass

    
def create_vault(usrid):
    print("Enter the image u want to be used as vault")
    template = input(":")
    print("Enter the path u want your image to be stored at")
    vault = input(":")
    name = input("name of the image:")
    os.system(f"touch {vault}/temp.txt")
    os.system(f"steghide embed -ef {vault}/temp.txt -cf {template} -sf {vault}/{name}.jpg -p {usrid} -f")
    os.system(f"rm {vault}/temp.txt")
    image_menu(usrid, {vault}/{name}.jpg)
    

def delete_vault():
    print("Are u sure ?\ntype 'yes' is so.")
    os.system("rm /root/workspace/github.com/justfancy64/password_manager/vault.jpg")
    print("vault and its data has been deleted")


if __name__ == "__main__":
    main()