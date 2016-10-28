# Nikolei Advani, 10/28/16
# This program takes an encoded or decoded message, and encodes or decodes it


def promptUser():
    """This function asks the user if they want to encode or decode a message"""
    print("e for encode, d for decode, q for quit")
    prompt = input("Would you like to encode or decode?")
    if prompt == "e":
        e = input("What would you like to encode?")
        encode(e)  # Encode function is called here
    elif prompt == "d":
        d = input("What would you like to decode?")
        decode(d)  # Decode function is called here
    else:
        print("Goodbye!")


def encode(e):
    """This function encodes the user's message"""
    number = int(input("What distance would you like to shift your text?"))
    string = "abcdefghijklmnopqrstuvwxyz"
    string2 = string[number:] + string[:number]
    string3 = ""
    for x in e.lower():
        if x == " ":
            string3 += " "
        else:
            corresponding = string.index(x)
            string3 += string2[corresponding]
            print(string3)


def decode(d):
    """This function decodes the user's message"""
    integer = int(input("Pick a number from 1-25"))
    string = "abcdefghijklmnopqrstuvwxyz"
    string2 = string[integer:] + string[:integer]
    string3 = ""
    for x in d.lower():
        if x == " ":
            string3 += " "
        else:
            corresponding = string2.index(x)
            string3 += string[corresponding]
    print(string3)


def main():
    """This function calls the promptUser function"""
    # The encode and decode functions are called in promptUser()
    promptUser()

main()
