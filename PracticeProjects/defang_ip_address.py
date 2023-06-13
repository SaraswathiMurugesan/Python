'''
Defanging IP Address:
A user’s IP address is defanged to prevent the user from clicking on a malicious link.
To convert an IP address to a defanged IP address, we need to replace “.” with “[.]”.
Here simply we need to treat “.” as a separator and split the string.
Then you have to rejoin an empty string and select “[.]” as the new separator:
'''

def ip_address(address):
    new_address = ""
    split_address = address.split(".")
    print(split_address)
    separator = "[.]"
    new_address = separator.join(split_address)
    return new_address
ipaddress = ip_address("1.1.2.3")
print(ipaddress)
