import getpass
import re
from passlib.hash import bcrypt_sha256


class Register:
    def __init__(self):
        self.password = None
        self.username = None
        self.hashed = None


    def add_user(self):
        print("\n[!] Username Must Be Between 4-10 Characters and Must Not Already Exist")
        self.username = input("Username: ")

        with open("secret.txt", "r") as f:
            for line in f:
                if line.strip():
                    key, value = [x.strip() for x in line.strip().split(':', 1)]
                    while self.username == key or len(self.username) < 4 or len(self.username) > 10:
                        print("[-] Username Already Exists or Your Username Does Not Meet Length Requirements")
                        self.username = input("Username: ")
                        if self.username != key:
                            return self.username
                        else:
                            continue
                        break
            f.close()


    def add_pass(self):
        print("\n[!] Minimum Password Requirements: 8-20 Characters, One Uppercase, One Special Character, One Number")
        while True:
            self.password = getpass.getpass(prompt="Password: ", stream=None)
            if re.search(r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,20}$", self.password) is None:
                print("[-] Password Does Not Meet Requirements")
                continue
            else:
                self.hashed = bcrypt_sha256.using(rounds=12).hash(self.password)
                print("\n[+] Account Created!")
                return self.hashed
            

    def write_file(self):
        with open("secret.txt", "a") as f:
            f.write(f"{self.username}:{self.hashed}\n")
        f.close()


class Login:
    def __init__(self):
        self.user_entry = None
        self.pass_entry = None

    def verify(self):
        attempts = 3
        self.user_entry = input("\nUsername: ")
        self.pass_entry = getpass.getpass(prompt="Password: ", stream=None)

        with open("secret.txt", "r") as f:
            for line in f:
                if line.strip():
                    key, value = [x.strip() for x in line.strip().split(':', 1)]
                    if bcrypt_sha256.verify(self.pass_entry, value):
                        print(f"\n[+] Welcome {self.user_entry}!")
                        return True    
                    elif not bcrypt_sha256.verify(self.pass_entry, value):
                        while attempts > 0:
                            print("[-] Invalid Username or Password")
                            self.user_entry = input("Username: ")
                            self.pass_entry = getpass.getpass(prompt="Password: ", stream=None)
                            attempts -= 1
                            if attempts == 0:
                                print("[-] Goodbye")
                            else:
                                continue
                            if bcrypt_sha256.verify(self.pass_entry, value):
                                print(f"\n[+] Welcome {self.user_entry}!")
                                return True
                            break
            f.close()


def main():
    new = Register()
    existing = Login()

    options = input("\nWould you like to login [1] or register [2]? ")
    if options == '1':
        existing.verify()
    elif options == '2':
        new.add_user()
        new.add_pass()
        new.write_file()
    else:
        print("[-] Invalid Option")
        exit(0)
       

if __name__=="__main__":
    main()