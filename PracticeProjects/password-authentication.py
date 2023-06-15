'''
password-authentication system
Password Authentication is the process of checking the identity of a user.
Almost every online platform today makes sure that they only give access to the real user
which can be only through authenticating the user with username and password.


'''

import getpass
userDictionary = {"aman.kharwal": "123456", "kharwal.aman": "654321"}  #Dictionary to hold username and password
username = input("Enter Your Username : ")
password = getpass.getpass("Enter Your Password : ")
for i in userDictionary.keys():
    if username == i:
        while password != userDictionary.get(i):
            password = getpass.getpass("Enter Your Password Again : ")
        break
print("Verified")
