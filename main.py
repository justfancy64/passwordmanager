import os
import filecmp
import bcrypt


def main():
    while True:

        account_check()
        userid = userid_check()
        menu(userid)



def add_password_to_vault(usrid, path):
        new_data = str(input("enter data for encryption:"))
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
    userid = str(f"{master_username}_{master_password}")
    encrypted_id = password_encyption(userid)
    print(encrypted_id)
    f = open("password_manager/bin/log.bin", "ab")
    f.write(encrypted_id)
    f.close()
    print("please log in using your username and password")
    account_check()

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
    usrid = str(f"{username}_{password}")
    if password_check(usrid):
        menu(usrid)
    else:
        print("WRONG CREDENTIALS")
        print("TRY AGAIN")
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
            pass
        case _:
            print("invalid input ")
            menu()


def image_menu(usrid, image_path):
    print("use 'view', 'add', 'clear'")
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



def password_encyption(usrid):
    byte_object = usrid.encode("utf-8")
    hashed = bcrypt.hashpw(byte_object, bcrypt.gensalt(14))
    print(hashed)
    return hashed

def password_check(usrid):
    byte_object = usrid.encode("utf-8")
    f = open("password_manager/bin/log.bin", "r")
    id_vault = f.read()
    lst = id_vault.split("$2b$14$")
    for line in lst:
        print(line)
        line2 = "$2b$14$" + line
        print(line2)
        bin = line2.encode("utf-8")
   
        if bcrypt.checkpw(byte_object, hashed_password=bin):
            return True
        else:
            return False


if __name__ == "__main__":
    main()